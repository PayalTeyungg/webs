from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    client_name=models.TextField()
    email = models.EmailField()
    contactnumber = models.CharField( max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit number.')]
    )
    message = models.TextField()


    def __str__(self):
        return self.email
    
class Hostel(models.Model):
    client_name=models.TextField()
    email = models.EmailField()
    contactnumber = models.CharField( max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit number.')]
    )
    message = models.TextField()


    def __str__(self):
        return self.email



    #     class Contact(models.Model):
    # client_name=models.TextField()
    # pet_name=models.TextField()
    # email = models.EmailField()
    # contactNummber = models.IntegerField()
    # release_date = models.DateField()

    # def __str__(self):
    #     return self.email

class Insurance(models.Model):
    client_id = models.AutoField(default=1),
    insurance_name = models.CharField(max_length=50),
    pet_name = models.CharField(max_length=50),
    owner_name = models.CharField(max_length=50),
    phone_number = models.models.PhoneNumberField(),
    startDate = models.DateField(),
    