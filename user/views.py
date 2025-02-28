from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import *
# from celery import shared_task

# Create your views here.
def home(request):
    return render(request,"home.html")


def register(request):
    if request.method=='POST':
        form=CustuserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('userlogin')
    else:
        form=CustuserRegistrationForm()
    return render(request,'register.html',{'form':form})


def vendorregister(request):
    if request.method=='POST':
        form=VendorRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('userlogin')
    else:
        form=VendorRegistrationForm()
    return render(request,'vendorregister.html',{'form':form})
            
    
def userlogin(request):
    if request.method=='POST':
        form=CustuserLoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('viewpackage')
    else:
        form=CustuserLoginForm(request.POST)
    return render(request,'login.html',{'form':form})


def userlogout(request):
    logout(request)
    return redirect('userlogin')


def viewpackage(request):
    package=Packages.objects.filter(approved=True)
    return render(request,'viewpackage.html',{'packages':package})


@login_required
def bookpackage(request,package_id):
    package=get_object_or_404(Packages,id=package_id,approved=True)
    if request.method=='POST':
        payment_id=request.POST.get("pl_PykvSullDf3eVN")
        if payment_id:
            booking=Booking(user=request.user,package=package)
            booking.save()
            return redirect('viewpackage')
    return render(request,'bookpackage.html',{'package':package})


# @shared_task
# def dltexpiredpackage():
#     Packages.objects.filter(expiry_date_lt=timezone.now()).delete()


@login_required
def addpackage(request):
    if request.user.role != 'vendor':
        return redirect('home')
    
    if request.method=='POST':
        form=PackagesForm(request.POST,request.FILES)
        if form.is_valid():
            package=form.save(commit=False)
            package.vendor=request.user
            package.save()
            return redirect('viewpackage')
    else:
        form=PackagesForm()
    return render(request,'addpackage.html',{'form':form})
    

@login_required
def editpackage(request,package_id):
    package=get_object_or_404(Packages, id=package_id)
    if request.method=='POST':
        form=PackagesForm(request.POST,request.FILES,instance=package)
        if form.is_valid():
            form.save()
            return redirect('viewpackage')
    else:
        form=PackagesForm(instance=package)
    return render(request,'editpackage.html',{'form':form})


@login_required
def deletepackage(request,package_id):
    package=get_object_or_404(Packages, id=package_id)
    if request.method=='POST':
       package.delete()
       return redirect('viewpackage')
    return render(request,'deletepackage.html',{'package':package})


# @user_passes_test(lambda u: u.is_authenticated and u.role=='admin')
def approvepackage(request,package_id):
    package=get_object_or_404(Packages,id=package_id,approved=False)
    package.approved=True
    package.save()
    return redirect('pendingpackage')


# @user_passes_test(lambda u: u.is_authenticated and u.role=='admin')
def pendingpackage(request):
    package=Packages.objects.filter(approved=False)
    return render(request,'pendingpackage.html',{'packages':package})









