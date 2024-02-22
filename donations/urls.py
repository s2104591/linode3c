"""
  Donations

"""
from . import views
from django.urls import path

urlpatterns = [
    path('donation', views.paymentgo , name="payment-go"),
    path('payment-success', views.paymentsuccess , name="payment-success"),
    path('payment-failure', views.paymentfailure , name="payment-failure"),




]
