from django import forms
from . models import Subscribers, MailMessage

class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]

# The mail messgae - all fiedls (title and message)
class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'
