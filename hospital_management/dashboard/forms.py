from django import forms
from .models import Patient_Base

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Patient_Base
        fields = '__all__'  # Use all fields from the Patient_Base model
