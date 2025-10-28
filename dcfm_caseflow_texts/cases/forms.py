# Original path: cases/forms.py


from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['number','year','case_type','category','complexity','urgency_level','public_interest','statutory_deadline']
        widgets = {
            'statutory_deadline': forms.DateInput(attrs={'type':'date'}),
        }
