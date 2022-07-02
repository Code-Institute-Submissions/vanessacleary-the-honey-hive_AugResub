from django.shortcuts import render
from . forms import SubscibersForm, MailMessageForm
from django.contrib import messages

# Create your views here.

def letter(request):
    if request.method == "POST":
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscription Successful")
            return redirect("/")
    else:
        form = SubscibersForm()
    context = {
        "form": form,
    }
    return render(request, "letter/letter.html", context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=["email"])
    mail_list = df["email"].values.tolist()
    print(mail_list)
    if request.method == "POST":
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get("title")
            message = form.cleaned_data.get("message")
            send_mail(
                title,
                message,
                "",
                mail_list,
                fail_silently=False,
            )
            messages.success(request, "Message has been sent to the Mail List")
            return redirect("mail-letter")
    else:
        form = MailMessageForm()
    context = {
        "form": form,
    }
    return render(request, "letter/mail_letter.html", context)
