
from . import views
from django.urls import path


urlpatterns = [
    path('tryWeb', views.tryWeb, name='tryWeb'),

    path('MainPage', views.MainPage, name='MainPage'),
    path('CreateCustomer', views.CreateCustomer, name='CreateCustomer'),
    path('AddNewMenu', views.AddNewMenu, name='AddNewMenu'),
    path('CustomerAccount', views.CustomerAccount, name='CustomerAccount'),
    path('AddMenu', views.AddMenu, name='AddMenu'),
    path('SaveUser', views.SaveUser, name='SaveUser'),
]