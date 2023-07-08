from .models import Contact
from .forms import ContactForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('index')

