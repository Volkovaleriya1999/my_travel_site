from .models import Comment
from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'captcha')
