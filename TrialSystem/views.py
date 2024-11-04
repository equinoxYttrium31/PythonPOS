from tempfile import template

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tryWeb(request):
    return HttpResponse("Hello World")

def MainPage(request):
    template = 'Practice_POS.html'
    context = {
        'title': 'Main Page',
        'body': 'This is the body of the main page.',
    }
    return render(request, template, context)