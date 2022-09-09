from socket import fromshare
from django import forms

class AddPage(forms.Form):
    title = forms.CharField(label='Title')
    text =  forms.CharField(label='Text', widget=forms.Textarea())