from django import forms
from .models import Task
from django.forms import DateTimeInput

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'priority', 'description', 'location', 'organizer', 'assigned_to']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
            'start_date': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input',
            }, format='%Y-%m-%dT%H:%M'),
            'end_date': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-input',
            }, format='%Y-%m-%dT%H:%M'),
            'priority': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Priority',
                'autocomplete': 'off'  # Disable autocomplete
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Description',
                'rows': 4,  # Adjust textarea height
                'cols': 40  # Adjust textarea width
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Location'
            }),
            'organizer': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Organizer'
            }),
            'assigned_to': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Assigned To'
            }),
        }
        labels = {
            'name': 'Task Name',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'priority': 'Priority',
            'description': 'Description',
            'location': 'Location',
            'organizer': 'Organizer',
            'assigned_to': 'Assigned To'
        }


    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # You can add more customization here if needed
