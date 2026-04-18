from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class Incident(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    CATEGORY_CHOICES = [
        ('Road', 'রাস্তা বা গর্ত'),
        ('Waste', 'ময়লা-আবর্জনা'),
        ('Electricity', 'বিদ্যুৎ বা ল্যাম্পপোস্ট'),
        ('Water', 'পানি বা ড্রেনেজ'),
    ]
    
    SEVERITY_CHOICES = [
        ('Low', 'কম গুরুত্ব'),
        ('Medium', 'মাঝারি'),
        ('High', 'অত্যধিক জরুরি'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='incidents/')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
