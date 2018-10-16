from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"index.html",{})

def work(request):
    return render(request,"nossotrabalho.html",{})

def aboutus(request):
    return render(request,"sobrenos.html",{})

def blog(request):
    return render(request,"blog.html",{})
