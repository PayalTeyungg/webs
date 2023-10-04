from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings
from .forms import InsurancePurchaseForm
from .models import InsurancePurchase

# Create your views here.


def servicepage(request):
     return render (request,'services.html')
    
def Homepage(request):
    return render (request,'landing.html')  

@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'landing.html')
    form = ContactForm()
    context = {'form': form}
    return render (request,'contact.html',context)  

def about(request):
    return render (request,'about.html')



def insurance(request):
    return render (request,'insurance.html')


@login_required(login_url='login')

def book(request):
    return render(request, 'book.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def Registerpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        


    return render (request,'register.html')     

def LogoutPage(request):
    logout(request)
    return redirect('home')
    

def food(request):
    return render(request,'food.html')

def hostel(request):
    return render(request,'hostel.html')

def insurance(request):
    return render(request,'insurance.html')
def booking(request):
    return render(request,'booking.html')
def purchase_insurance(request, plan_id):
    # Get the selected insurance plan
    insurance_plan = get_object_or_404(InsurancePlan, id=plan_id)
    
    if request.method == 'POST':
        form = InsurancePurchaseForm(request.POST)
        if form.is_valid():
            # Generate a unique transaction ID
            transaction_id = generate_transaction_id()
            
            # Create a record of the insurance purchase
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.insurance_plan = insurance_plan
            purchase.transaction_id = transaction_id
            purchase.save()
            
            # Construct the payment request data
            payload = {
                'public_key': settings.KHALTI_PUBLIC_KEY,
                'amount': insurance_plan.premium_amount,
                'product_identity': transaction_id,
                'product_name': f"Insurance - {insurance_plan.name}",
                'product_url': request.build_absolute_uri(reverse('insurance_purchase_success')),
            }
            
            # Send the payment request to Khalti
            response = requests.post('https://khalti.com/api/v2/payment/initiate', data=payload)
            
            if response.status_code == 200:
                data = response.json()
                # Redirect to the Khalti payment page
                return redirect(data['redirect'])
            else:
                # Handle the error
                return render(request, 'insurance/error.html', {'error_message': 'Payment initiation failed.'})
    else:
        form = InsurancePurchaseForm()
    
    return render(request, 'insurance/purchase.html', {'form': form, 'insurance_plan': insurance_plan})

def purchase_success(request):
    # Handle the success callback from Khalti
    transaction_id = request.GET.get('product_identity')
    purchase = get_object_or_404(InsurancePurchase, transaction_id=transaction_id)
    
    # Update the payment status
    purchase.payment_status = True
    purchase.save()
    
    return render(request, 'insurance/purchase_success.html', {'purchase': purchase})