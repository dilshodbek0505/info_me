from django.shortcuts import render, redirect

from .models import Info

def home(request, username):
    try: 
        info = Info.objects.get(username = username)
        return render(request, 'home.html', {"info": info})
    except:
        print("error")

def qr_code(request, username):
    try: 
        info = Info.objects.get(username = username)
        return render(request, 'qr_code.html', {"image": info.qr_code})
    except:
        print("error")