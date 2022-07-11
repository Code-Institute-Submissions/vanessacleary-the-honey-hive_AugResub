from django.shortcuts import render, redirect, reverse
from . models import Subscribers
from django.contrib import messages

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
