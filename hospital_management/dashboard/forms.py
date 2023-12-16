from django import forms
from .models import Patient_Base, BedOccupancy
        
class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Patient_Base
        fields = '__all__' # Use all fields from the Patient_Base model

class BedForm(forms.ModelForm):
    class Meta:
        model = BedOccupancy
        fields = '__all__'  # Use all fields from the BedOccupancy model