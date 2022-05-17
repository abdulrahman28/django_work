from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import detail
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.

def index(request):

    return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        uname = request.POST['uname']
        email = request.POST['email']
        pword = request.POST['pword']
        cpword = request.POST['cpword']
        dept = request.POST['dept']

        if pword == cpword:

            if User.objects.filter(username=uname).exists():
                messages.info(request, uname + ', already exist, Try another Username!!!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, email + ', already exist, Try another Email Address!!!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=uname, email=email, password=pword)
                lg = detail.objects.create(uname=uname, dept=dept)
                user.save()
                lg.save()
                return redirect('signin')
                
        else:
            messages.info(request, 'Password does not match!!!')
            return redirect('register')
    else:
        return render(request,'register.html')

def signin(request):   
    if request.method == 'POST':

        uname = request.POST['uname']
        pword = request.POST['pword']

        user = auth.authenticate(username=uname, password=pword)

        if user is not None:
            auth.login(request, user)
            return redirect('.')

        else:
            messages.info(request, 'Invalid Login Details!!!')
            return redirect('signin')


    else:
        return render(request,'signin.html')


def settings(request):

     return render(request,'settings.html')   
        


def change(request):   
 if request.method == 'POST':

       Name = request.POST[' Name']
       Newname = request.POST['Newname']
       email = request.POST[' email']
       Newemail = request.POST['Newemail']
       Dprtm = request.POST[' Dprtm']
       Newdprtm = request.POST['Newdprtm']
       
       if Name == Newname:

              if User.objects.filter(Name=Newname).exists():
                     messages.info(request, Name + ', already exist, Try another Username!!!')
                     return redirect('settings')

              elif User.objects.filter(email=Newemail).exists():
                    messages.info(request, email + ', already exist, Try another Email Address!!!')
                    return redirect('settings')

              else:
                  user = User.objects.create_user(name=Newname, email=Newemail)
                  lg = detail.objects.create(name=Newname, Dprtm=Dprtm)
                  user.save()
                  lg.save()
                  return redirect('settings')

       else:
            messages.info(request, ' pls write the correct name!!!')
            return redirect('settings')
 else:
    return render(request,'change.html')   


def changepassword(request):

    if request.method == 'POST':

        pword = request.POST['pword']
        cpword = request.POST['cpword']
        

        if pword == cpword:

             messages.info(request, cpword + ', has been changed successfully!!!')
             return redirect('change')

            
        else:
            messages.info(request, 'Password does not match!!!')
            return redirect('changepassword')
    else:
        return render(request,'changepassword.html')         






