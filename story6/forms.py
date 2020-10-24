from django import forms
from .models import Activity, Participant

class Act_Form(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['actname']
    error_messages = {
        'required' : 'Please Type'
    }

    actname = forms.CharField(label="Activity Name", max_length=30)

class Par_Form(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'contact_number']
    error_messages = {
        'required' : 'Please Type'
    }
    # activ_name = forms.ModelMultipleChoiceField(queryset=Activity.objects.all())
    # name = forms.CharField(label = "Name", max_length = 20)
    # con_num = forms.CharField(label = "Contact Number", max_length=12)