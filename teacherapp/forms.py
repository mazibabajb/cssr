from django import forms
from django.contrib.auth.models import User
from .models import Registration,Contact

class regform(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
       

class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
       
	

    