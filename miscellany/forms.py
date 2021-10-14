from django import forms
from .models import ContactMe

class reachout(forms.ModelForm):
    class Meta:
        model = ContactMe
        exclude = ['pub_date']