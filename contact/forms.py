from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Create ContactForm class """

    class Meta:
        """ Update Class Meta Data """
        model = Contact
        exclude = ('user', 'message_sent')

    def __init__(self, *args, **kwargs):
        """ Add placeholders and required attribute,
        set autofocus on first field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'e.g Ruby Boyd ',
            'email_form': 'e.g Rubyboyd@gmail.com',
            'order_number': 'E7g5VQWNEdc9Zsb',
            'enquiry': 'Hello, how long does it take to deliver to Australia'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder 