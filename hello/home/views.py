from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

def index(request):
    context = {
        "variable1": "this is a temp variable1",
        "variable2": "this is a temp variable2",

    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page!")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your details have been recorded')
    return render(request, 'contact.html')
