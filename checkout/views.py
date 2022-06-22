from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L4npfG2WfYWNVK0teHNpX1kTcc5ElDYxvpxv2OJigTqoU9V8ud0hdPnQ2S1lRMBYvQglHFmfaB2MgWBAaR0w59K00M4uqbPxL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

 