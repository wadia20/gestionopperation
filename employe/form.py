from django import forms
from .models import Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['client_id', 'operation', 'observation', 'piece_jointe', 'confirmed']


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['client_id', 'operation', 'piece_jointe', 'observation', 'confirmed']