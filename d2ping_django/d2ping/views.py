from django.shortcuts import render
from d2ping.scripts.d2ping import *
# Create your views here.

def index(request):
    context = {
        'sevinfo': sevinfoall
    }

    return render(request,'d2ping/home.html',context)
def checkping(request):
    sevinfo = pingfoo()
    

    context = {
        'sevinfo': sevinfo
    }

    return render(request,'d2ping/home.html',context)
