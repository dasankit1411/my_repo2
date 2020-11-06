"""consultant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from consultapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('admin_login/', views.Login,name='login'),
    path('logout/', views.Logout,name='logout'),
    path('contactus/', views.contactus,name='contactus'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('addorganisation/', views.addorganisation,name='addorganisation'),
    path('vieworganisation/', views.vieworganisation,name='vieworganisation'),
    path('deleteorganisation(?P<int:pk>)', views.deleteorganisation,name='deleteorganisation'),
    path('addexpert/', views.addexperts,name='addexperts'),
    path('viewexpert/', views.viewexperts,name='viewexperts'),
    path('deleteexpert(?P<int:pk>)', views.deleteexpert,name='deleteexpert'),
    path('updateexp(?P<int:pk>)', views.editexpert,name='updateexp'),
    path('updateorg(?P<int:pk>)', views.editoraganisation,name='updateorg'),


]
