from django import forms
from consultapp.models import *

class OrganisationForm(forms.ModelForm):
    class Meta:
        model=Organisation
        fields='__all__'

class ExpertForm(forms.ModelForm):
    class Meta:
        model=Expert
        fields='__all__'
