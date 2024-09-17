from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')
