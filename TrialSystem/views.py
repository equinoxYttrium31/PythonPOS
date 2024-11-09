from django.urls import reverse
from tempfile import template

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

# Create your views here.
def tryWeb(request):
    return HttpResponse("Hello World")

def MainPage(request):
    menuList = models.Menu.objects.all()
    template = 'Practice_POS.html'
    context = {
        'title': 'Main Page',
        'body': 'This is the body of the main page.',
        'menuItems': menuList,
    }
    return render(request, template, context)

def CreateCustomer(request):
    template = 'Create_Customer_Account.html'
    return render(request, template)

def CustomerAccount(request):
    customers = models.Customer.objects.all()
    template = 'Customer_List.html'
    context = {
        'customers': customers,
    }
    return render(request, template, context)



def SaveUser(request):
    customer = models.Customer()
    customer.CustomerNumber = request.GET['CustomerNumber']
    customer.CustomerName = request.GET['CustomerName']
    customer.CustomerEmail = request.GET['CustomerEmail']
    customer.save()

    return HttpResponseRedirect(reverse('CustomerAccount'))