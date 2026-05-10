from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    """
    Form for creating and updating urban incidents.
    Coordinates are set to readonly as they are managed by the map API.
    """
    class Meta:
        model = Incident
        # Including all necessary fields from the model
        fields = [
            'title', 'description', 'category', 'location', 
            'image', 'severity', 'latitude', 'longitude'
        ]
        
        # Defining widgets with Bootstrap classes for professional UI
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a concise headline for the issue'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Provide detailed information about the problem'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Street name, landmark, or area'
            }),
            'severity': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            
            # Readonly GPS coordinates to ensure data integrity from the map
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control bg-light', 
                'placeholder': 'Auto-filled latitude', 
                'readonly': 'readonly'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control bg-light', 
                'placeholder': 'Auto-filled longitude', 
                'readonly': 'readonly'
            }),
        }