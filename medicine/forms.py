from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        fields= ["Id","M_Name","M_Type","Mnf_Date","Exp_Date","MRP","Stock"]
