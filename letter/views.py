from django.shortcuts import render
from . forms import SubscibersForm, MailMessageForm

# Create your views here.

def letter(request):
      if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
  return render(request, 'letter.html', context)