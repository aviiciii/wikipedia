from socket import fromshare
from django import forms

class AddPage(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    text =  forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'form-control'}
    ))

class EditPage(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    text =  forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'form-control', 'required':'False'}
    ))
    