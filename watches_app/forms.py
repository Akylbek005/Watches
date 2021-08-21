from django import forms
from .models import Contact, EmailNewsLetter


class ContactForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = Contact


class EmailNewsLetterForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = EmailNewsLetter
