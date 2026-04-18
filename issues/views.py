from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Incident
from .forms import IncidentForm

# ১. একাউন্ট তৈরি (Register)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ২. হোমপেজ ড্যাশবোর্ড (Home)
def home(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    
    incidents = Incident.objects.all().order_by('-created_at')

    if query:
        incidents = incidents.filter(title__icontains=query)
    if category_filter:
        incidents = incidents.filter(category=category_filter)

    stats = Incident.objects.values('category').annotate(total=Count('id'))
    severity_stats = Incident.objects.values('severity').annotate(total=Count('id'))

    context = {
        'incidents': incidents,
        'stats': stats,
        'severity_stats': severity_stats,
    }
    return render(request, 'issues/home.html', context)

# ৩. সমস্যা রিপোর্ট করা (Report - Login Required)
@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.author = request.user # যে লগইন করা আছে তাকে লেখক বানানো হলো
            incident.save()
            messages.success(request, 'আপনার রিপোর্টটি সফলভাবে জমা হয়েছে!')
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'issues/report.html', {'form': form})

# ৪. বিস্তারিত রিপোর্ট দেখা (Detail)
def issue_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'issues/detail.html', {'incident': incident})

# ৫. আমার করা রিপোর্টগুলো দেখা (My Reports)
@login_required
def my_reports(request):
    reports = Incident.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'issues/my_reports.html', {'reports': reports})

# ৬. রিপোর্ট ডিলিট করা (Delete)
@login_required
def delete_report(request, pk):
    report = get_object_or_404(Incident, pk=pk, author=request.user)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'রিপোর্টটি সফলভাবে ডিলিট করা হয়েছে।')
        return redirect('my_reports')
    return render(request, 'issues/delete_confirm.html', {'report': report})

# ৭. স্ট্যাটাস আপডেট করা (Update Status - Admin/Staff Only)
@login_required
def update_status(request, pk):
    if not request.user.is_staff: # চেক করা হচ্ছে সে অ্যাডমিন কি না
        return redirect('home')
    
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        incident.status = new_status
        incident.save()
        messages.success(request, f'স্ট্যাটাস আপডেট করে {new_status} করা হয়েছে!')
        return redirect('issue_detail', pk=pk)