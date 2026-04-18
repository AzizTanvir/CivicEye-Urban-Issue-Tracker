from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'category', 'location', 'image', 'severity']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'সমস্যার শিরোনাম'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'বিস্তারিত বর্ণনা লিখুন'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'এলাকার নাম বা ঠিকানা'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }