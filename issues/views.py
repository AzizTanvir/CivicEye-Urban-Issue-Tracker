from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Incident
from .forms import IncidentForm

# 1. Handle user registration
def register(request):
    """View to handle new user account creation."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# 2. Main Dashboard (Map and Charts)
def home(request):
    """View to display reports on the map and analytics charts."""
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    
    incidents = Incident.objects.all().order_by('-created_at')

    # Apply search and category filters
    if query:
        incidents = incidents.filter(title__icontains=query)
    if category_filter:
        incidents = incidents.filter(category=category_filter)

    # Data for Chart.js analytics
    stats = Incident.objects.values('category').annotate(total=Count('id'))
    severity_stats = Incident.objects.values('severity').annotate(total=Count('id'))

    context = {
        'incidents': incidents,
        'stats': stats,
        'severity_stats': severity_stats,
    }
    return render(request, 'issues/home.html', context)

# 3. Report a new Incident
@login_required
def report_issue(request):
    """View to allow logged-in users to submit a new report."""
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.author = request.user # Assign current user as author
            incident.save()
            messages.success(request, 'Your report has been successfully posted!')
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'issues/report.html', {'form': form})

# 4. Incident Detailed View
def issue_detail(request, pk):
    """View to display the complete details of a single incident."""
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'issues/detail.html', {'incident': incident})

# 5. User Specific Reports
@login_required
def my_reports(request):
    """View to display reports submitted by the logged-in user."""
    reports = Incident.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'issues/my_reports.html', {'reports': reports})

# 6. Delete a Report
@login_required
def delete_report(request, pk):
    """View to allow users to delete their own reports."""
    report = get_object_or_404(Incident, pk=pk, author=request.user)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'The report has been successfully deleted!')
        return redirect('my_reports')
    return render(request, 'issues/delete_confirm.html', {'report': report})

# 7. Administrative Status Update
@login_required
def update_status(request, pk):
    """View to allow staff members to update incident status."""
    if not request.user.is_staff: # Authorization check
        return redirect('home')
    
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        incident.status = new_status
        incident.save()
        messages.success(request, f'Incident status successfully updated to {new_status}!')
        return redirect('issue_detail', pk=pk)