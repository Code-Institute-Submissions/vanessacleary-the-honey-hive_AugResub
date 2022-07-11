from django.shortcuts import render, redirect, reverse
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail

def handle_subscription(request):
    if request.method == "POST":
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscription Successful")
            return redirect(reverse('home'))
    else:
        form = SubscibersForm()
    context = {
        "form": form,
    }
    return render(request, "letter/letter.html", context)
