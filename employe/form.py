from django import forms
from .models import Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['client_id', 'operation', 'operation_date', 'observation', 'piece_jointe', 'confirmed']
