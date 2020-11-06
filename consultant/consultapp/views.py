from django.shortcuts import render,redirect
from consultapp.forms import *
from consultapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
    return render(request,'consult/home.html')

def Login(request):
    error=''
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'consult/login.html',d)

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def contactus(request):
    return render(request,'consult/contactus.html')

def aboutus(request):
    return render(request,'consult/aboutus.html')

def addorganisation(request):
    if not request.user.is_staff:
        return redirect("login")
    form=OrganisationForm()
    if request.method=="POST":
        form=OrganisationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vieworganisation')
    d={"form":form}
    return render(request,'consult/addorganisation.html',d)

def vieworganisation(request):
    if not request.user.is_staff:
        return redirect('login')
    org=Organisation.objects.all()
    d={'org':org}
    return render(request,'consult/view_organisation.html',d)

def deleteorganisation(request,pk):
    if not request.user.is_staff:
        return redirect('login')
    org=Organisation.objects.get(id=pk)
    org.delete()
    return redirect('vieworganisation')

def addexperts(request):
    if not request.user.is_staff:
        return redirect("login")
    form=ExpertForm()
    if request.method=="POST":
        form=ExpertForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('viewexperts')
    d={"form":form}
    return render(request,'consult/addexperts.html',d)

def viewexperts(request):
    if not request.user.is_staff:
        return redirect('login')
    exp=Expert.objects.all()
    d={'exp':exp}
    return render(request,'consult/viewexperts.html',d)

def deleteexpert(request,pk):
    if not request.user.is_staff:
        return redirect('login')
    exp=Expert.objects.get(id=pk)
    exp.delete()
    return redirect('viewexpert')

def editexpert(request,pk):
    if not request.user.is_staff:
        return redirect('login')
    #if viewexperts(request):
    exp=Expert.objects.get(id=pk)
    if request.method=="POST":
        form=ExpertForm(request.POST,instance=exp)
        if form.is_valid():
            form.save()
            return redirect('viewexperts')
    return render(request,'consult/update.html',{'exp':exp})
    #elif vieworganisation(request):
def editoraganisation(request,pk):
    org=Organisation.objects.get(id=pk)
    if request.method=="POST":
        form=OrganisationForm(request.POST,instance=org)
        if form.is_valid():
            form.save()
            return redirect('vieworganisation')
    return render(request,'consult/updateorganisation.html',{'org':org})
