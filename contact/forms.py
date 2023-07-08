from django import forms
from .models import Contact
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """Форма подписки на email"""
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'captcha')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'newsletter_input newsletter_input_name',
                                           'id': 'newsletter_input_name', 'placeholder': 'Имя', 'required':
                                               True}),
            'email': forms.EmailInput(attrs={'class': 'newsletter_input newsletter_input_email',
                                             'id': 'newsletter_input_email', 'placeholder': 'Email', 'required':
                                               True}),
        }
        labels = {
            'email': '',
            'name': '',
        }








