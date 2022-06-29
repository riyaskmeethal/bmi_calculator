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

    meters = forms.FloatField(required=False  ,label='',widget=forms.TextInput(attrs={'placeholder': 'Meter'}) )
    centi_meters = forms.FloatField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'Centi meters'}))
    foots = forms.FloatField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'Foots'}))
    inches = forms.FloatField(required=False,label='',widget=forms.TextInput(attrs={'placeholder': 'Inches'}))

    class Meta:
        model = BmiModel
        fields = ['name','age','weight',]