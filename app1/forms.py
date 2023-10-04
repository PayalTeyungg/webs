from django.forms import ModelForm
from .models import Contact
from .models import Insurance

class ContactForm(ModelForm):
  class Meta:
      model = Contact
      fields = '__all__'
     
class Insuranceform(ModelForm):
   class Meta:
      model = Insurance
      fields='__all__'