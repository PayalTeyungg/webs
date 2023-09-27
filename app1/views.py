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

