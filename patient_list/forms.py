from django import forms
from .models import PatientDetails

class DetailsInput(forms.ModelForm):
   class Meta:
       model = PatientDetails
       fields = ['serial','name','doctor',]
       widgets = {
            'serial' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor' : forms.TextInput(attrs={'class':'form-control'}),
        }