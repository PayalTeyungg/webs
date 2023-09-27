"""
URL configuration for Petcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

admin.site.site_header = 'Pet Care'
admin.site.site_title = 'Pet Care'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='home'),
    path('register/',views.Registerpage,name='register'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('dashboard/',views.Dashboard,name='dashboard'),
    path('services/',views.servicepage,name='services'),
    path('about/',views.about,name='about'),
      path('contact/',views.contact,name='contact'),
        path("book/",views.book,name='book'),
        path("food/",views.food,name="food"),
        path("insurance/",views.insurance,name="insurance"),
        path("hostel/",views.hostel,name="hostel"),
        path("booking/",views.booking,name='booking'),

]



