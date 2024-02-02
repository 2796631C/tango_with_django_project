from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse

def index(request):
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'about_url' : reverse('about'),
    }
    return render(request, 'rango/index.html', context=context_dict)

    #return HttpResponse("Rango says hey there partner!")

def about(request):
    context_dict = {
        'boldmessage': 'This tutorial has been put together by Camilla.',
        'index_url' : reverse('index')
}
    return render(request, 'rango/about.html', context=context_dict)