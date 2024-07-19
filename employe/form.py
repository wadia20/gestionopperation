from django import forms
from .models import Operation,Client

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['client_id', 'operation', 'observation', 'piece_jointe', 'confirmed']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_Name', 'Date_Of_Birth', 'Phone', 'Email', 'Gender', 'Address']
