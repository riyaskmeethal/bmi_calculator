from django.forms import ModelForm
from .models import BmiModel
from django import forms
scales = (("meter","Meter"),("foot",'Foot'))

CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
    ("others", "Others"),)
class BmiForm(ModelForm):
    gender = forms.ChoiceField(choices = CHOICES)
    scale = forms.ChoiceField(choices=scales, widget=forms.RadioSelect())

    class Meta:
        model = BmiModel
        fields = '__all__'