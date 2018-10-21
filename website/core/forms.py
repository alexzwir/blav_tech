from django import forms
from django.utils import timezone


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,label="Nome")
    contact_email = forms.EmailField(max_length=30,label="Email")
    contact_phone = forms.CharField(max_length=30,label="Telefone")
    contact_message = forms.CharField(max_length=500,label="Mensagem")