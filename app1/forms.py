from django.forms import ModelForm
from .models import Contact
from django import forms
from .models import InsurancePurchase


class ContactForm(ModelForm):
  class Meta:
      model = Contact
      fields = '__all__'
     

class InsurancePurchaseForm(forms.ModelForm):
    class Meta:
        model = InsurancePurchase
        fields = []

    