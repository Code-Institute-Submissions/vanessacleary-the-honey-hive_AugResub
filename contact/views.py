from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile
from .forms import ContactForm
from .models import Contact
import logging


log = logging.getLogger(__name__)


def contact(request):
    """ A view to render the contact page """

    if request.method == 'POST':
        # If post method successful get information from form
        form_data = {
            'full_name': request.POST['full_name'],
            'email_from': request.POST['email_from'],
            'order_number': request.POST['order_number'],
            'enquiry': request.POST['enquiry'],
        }
        contact_form = ContactForm(form_data)
        # If form valid, save enquiry
        if contact_form.is_valid():
            user_enquiry = contact_form.save(commit=False)
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user)
                user_enquiry.user = user
            user_enquiry.save()

            try:
                # Send confirmation email to user
                log.info("Sending email")
                send_confirmation_email(user_enquiry)
            except Exception as e:
                if request.user.is_authenticated and request.is_superuser:
                    messages.error(request, 'There was an error with the enquiry. Check Logs.')
                log.exception(f"Exception occurred when sending email: {str(e)}")

            messages.success(request,
                             'Your enquiry has been sent.'
                             'Check your emails for a confirmation')
            return redirect(reverse('home'))
        # If not valid, error message displayed
        else:
            messages.error(request,
                           'There was an error with your enquiry.'
                           'Please ensure the form is valid')
            return redirect(reverse('contact'))
    else:
        if request.user.is_authenticated:
            # If user is logged in try and populate information
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                   # 'full_name': profile.default_full_name,
                    'full_name': profile.user.username, # the above field caused an issue and would not allow me to submit a contact form (bug only came out as I previosly could submit a contact form) - I added new model and migrated and this option now works - I updated line 15 in profile/models
                    'email_from': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
        template = 'contact/contact.html'
        context = {
            'contact_form': contact_form,
        }

        return render(request, template, context)


def send_confirmation_email(user_enquiry: Contact):
    """ Send a confirmation email to user following successful enquiry """
    cust_email = user_enquiry.email_from
    subject = 'Thank you for contacting The Honey Hive'
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'contact': user_enquiry})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
    # Send email to admin notifying of new contact message
    send_mail(
        f"You have received an enquiry from { user_enquiry.full_name }",
        user_enquiry.enquiry,
        user_enquiry.email_from,
        [settings.DEFAULT_FROM_EMAIL],
    )