from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "variable1": "this is a temp variable1",
        "variable2": "this is a temp variable2",

    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page!")

def about(request):
    return HttpResponse("This is about page!")

def services(request):
    return HttpResponse("This is services page!")

def contact(request):
    return HttpResponse("This is contact page!")