from django import forms
from django.utils import timezone


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={'placeholder': 'Nome','size': '50',"class":"form-control"}))
    contact_email = forms.EmailField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'Email','size': '50',"class":"form-control"}))
    contact_phone = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'Telefone','size': '50',"class":"form-control"}))
    contact_message = forms.CharField(max_length=500,label="",widget=forms.Textarea(attrs={'placeholder':'Deixe sua mensagem aqui',"class": "form-control"}))


"""
Took out the label and insert the placeholder for forms
contact_phone = forms.CharField(max_length=30,label="Telefone")
"""