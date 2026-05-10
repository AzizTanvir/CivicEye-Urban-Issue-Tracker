from django.db import models
from django.contrib.auth.models import User

# Model to store reported urban issues with geospatial data
class Incident(models.Model):
    # Category options for the reported issues
    CATEGORY_CHOICES = [
        ('Road or Hole', 'Road or Hole'),
        ('Waste or Garbage', 'Waste or Garbage'),
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
    ]
    
    # Severity levels to prioritize the issues
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # Status tracking for administrative actions
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Solved', 'Solved'),
    ]

    # Relationships and Fields
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255) # General area description
    
    # Geospatial data for precise mapping
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    image = models.ImageField(upload_to='incidents/')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title