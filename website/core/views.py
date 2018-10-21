from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import ContactModel

# Create your views here.


def home(request):
    return render(request,"index.html",{})

def work(request):
    return render(request,"nossotrabalho.html",{})

def aboutus(request):
    return render(request,"sobrenos.html",{})

def blog(request):
    return render(request,"blog.html",{})

def contact(request):
    form = ContactForm()
    return render(request,"contato.html",{"form":form})

def saving_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contato_enviado = ContactModel(contact_name = form.cleaned_data['contact_name'],contact_email = form.cleaned_data['contact_email'],contact_phone = form.cleaned_data['contact_phone'],contact_message = form.cleaned_data['contact_message'])
        contato_enviado.save()
    return HttpResponseRedirect('/')

"""
MODEL
contact_name = models.CharField(max_length=50)
contact_email = models.EmailField(max_length=30)
contact_phone = models.CharField(max_length=30)
contact_sent_date = models.DateTimeField(max_length=35,default=timezone.now)
contact_message = models.TextField(max_length=500)

FORM
contact_name = forms.CharField(max_length=50,label="Nome")
contact_email = forms.EmailField(max_length=30,label="Email")
contact_phone = forms.CharField(max_length=30,label="Telefone")
contact_message = forms.CharField(max_length=500,label="Mensagem")
"""
