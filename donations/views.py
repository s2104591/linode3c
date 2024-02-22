from django.shortcuts import render
from django.urls import reverse

from django.conf import settings

import stripe
import uuid


#from . models import Donation

# Create your views here.




def paymentsuccess(request):
    return render(request,"donations/payment-success.html")



def paymentfailure(request):
    return render(request,"donations/payment-failed.html")

###############

def paymentgo(request):
    #return render(request,"donations/my-donation.html")

 
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
    line_items=[{

        #'price': 'price_1NJf9qIwkDjL5wroiZ0dl0TV', # Enter your API ID here  
        "price":"price_1OjqrgBZLl5LK1PpRDyp4JfI",   
        "price":"price_1OjqrgBZLl5LK1PpRDyp4JfI",   
        'quantity': 1,
    
    }],

    mode='payment',
    
    success_url=request.build_absolute_uri(reverse('payment-success')) + '?session_id={CHECKOUT_SESSION_ID}',
    
    cancel_url=request.build_absolute_uri(reverse('payment-failure'))
    
    )

    #return render(request, 'donation/my-donation.html', {'paypal_form': paypal_form})
    return render(request, 'donations/my-donation.html', {'session_id':session.id, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY} )







