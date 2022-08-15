from datetime import datetime
from logging import error
from Hello.models import Contact,User
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from Hello.forms import MyUserCreationForm,UserForm
from multiprocessing import context
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date = datetime.today()
        contact = Contact(name = name, email = email,message = message,date = date)
        if contact:
            contact.save()
            messages.success(request,"Your message was send!")
            return redirect("/")
        else:
            message.success(request,"There was an error")
            return redirect("/contact")
    return render(request,'contact.html')

def login_user(request):
    if request.user.is_authenticated:
        messages.success(request,"You have already login")
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        user = authenticate(request,email = email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully!")
            return redirect("/")
        else:
            messages.success(request,"Invalid Credentials")
            return redirect('/login')

    return render(request,'login.html')


def signup_user(request):
    if request.user.is_authenticated:
        messages.success(request,"You have already signup")
        return redirect("/")

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request,user)
            messages.success(request,"Registeration was successfull!")
            return redirect("/")
        else:
            messages.success(request,"There was a error in registertaion, plz fill the form again")
            return redirect("/signup")

    form = MyUserCreationForm()
    context = {'form':form}
    return render(request,"signup.html",context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfully...")
    return redirect("/login") 


@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {'user':user}
    return render(request,'profile.html',context)

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES, instance = user)
        username = form.data.get('username')
        post_email = form.data.get('email')
        if form.is_valid():
            form.save()
            messages.success(request,"Your profile has been updated successfully!")
            return redirect("/profile")
        else:
            messages.success(request,"Ther was an error, plz try again")   
            return redirect("/edit_profile")
    form = UserForm(instance=user)
    context = {'form':form}
    return render(request,"edit_profile.html",context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) # import!
            messages.success(request,"Your password has been changed")
            return redirect("/profile")
        else:
            messages.success(request,"There was an error, plz satisfy the follwing two requirements *")
            return redirect("/change_password")
    form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request,"change_password.html",context)


