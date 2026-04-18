from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from issues import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report_issue'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    
    # "আমার রিপোর্ট" এবং "ডিলিট" এর জন্য নতুন পাথ
    path('my-reports/', views.my_reports, name='my_reports'),
    path('delete/<int:pk>/', views.delete_report, name='delete_report'),
    path('update-status/<int:pk>/', views.update_status, name='update_status'),
    
    # একাউন্ট সিস্টেম
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)