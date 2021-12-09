from django.urls import path
from . import views

urlpatterns = [
    path ('make-deposit/', views.deposit, name='deposit'),
    path ('btc-converter/', views.currency_converter, name='btc'),
    path('testing-api/', views.testing_api, name='testing'),
]