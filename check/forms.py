from django import forms
from .models import Bmi
 
class CreateBmi(forms.ModelForm):
    class Meta:
        model = Bmi
 
        fields = ['name', 'height', 'weight']