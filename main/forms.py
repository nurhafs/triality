from django import forms
from .models import Course

class Input_Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'lecturer', 'sks', 'desc', 'year', 'kls']
    error_messages = {
        'required' : 'Please Type'
    }

    name = forms.CharField(label="Name", max_length=50)
    lecturer = forms.CharField(label="Lecturer", max_length=25)
    sks = forms.CharField(label="Amount of Credits", max_length=2)
    desc = forms.CharField(label="Description", max_length=200)
    year = forms.CharField(label="Academic Year", max_length=20)
    kls = forms.CharField(label="Classroom", max_length=10)
