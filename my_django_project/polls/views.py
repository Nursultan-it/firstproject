from django.shortcuts import render, redirect
from .models import *
from .forms import Clothesform, Customsform,UserForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage

# from .forms import NewUserForm

from django.contrib.auth import login as auth_login

def customs(request):
    customs = Customs.objects.all
    return render(request, "customs.html", {'title': 'Traditional Customs', 'customs': customs})


def home(request):
    home = Home.objects.all
    return render(request, "home.html", {'title': 'Home page', 'home': home, })


def about(request):
    about = Questions.objects.all
    return render(request, "about.html", {'title': 'About', 'about': about, })


def registration(request):
    return render(request, "registration.html", {'title': 'Registration'})


def login(request):
    return render(request, "login.html", {'title': 'login'})


def create_clothes(request):
    form = Clothesform()
    if request.method == "POST":
        form = Clothesform(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_clothes')
            except:
                message = "Something we are wrong!"
                form = Clothesform()
            return render(request, 'create.html', {'message': message, 'form': form})
    else:
        form = Clothesform()
    return render(request, 'create.html', {'form': form})


def show_clothes(request):
    cloth = Clothes.objects.order_by('id')
    return render(request, 'index.html', {'cloth': cloth})


def edit_clothes(requst, id):
    cloth = Clothes.objects.get(id=id)
    return render(requst, 'edit.html', {'cloth': cloth})


def update_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    if request.method == "POST":
        form = Clothesform(request.POST, request.FILES, instance=cloth)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_clothes")
        message = 'Something we are wrong!'
        return render(request, 'edit.html', {'message': message, 'cloth': form})
    else:
        form = Clothes.objects.get(id=id)
        cloth = Clothesform(instance=form)
        content = {'cloth': cloth, 'id': id}
        return render(request, 'edit.html', content)


def delete_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    cloth.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_clothes")


def create_customs(request):
    form = Customsform()
    if request.method == "POST":
        form = Customsform(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_customs')
            except:
                message = "Something we are wrong!"
                form = Customsform()
            return render(request, 'create2.html', {'message': message, 'form': form})
    else:
        form = Clothesform()
    return render(request, 'create2.html', {'form': form})


def show_customs(request):
    custom = Customs.objects.order_by('id')
    return render(request, 'index2.html', {'custom': custom})


def edit_customs(requst, id):
    custom = Customs.objects.get(id=id)
    return render(requst, 'edit2.html', {'custom': custom})


def update_customs(request, id):
    custom = Customs.objects.get(id=id)
    if request.method == "POST":
        form = Customsform(request.POST, request.FILES, instance=custom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_customs")
        message = 'Something we are wrong!'
        return render(request, 'edit2.html', {'message': message, 'custom': form})
    else:
        form = Customs.objects.get(id=id)
        custom = Customsform(instance=form)
        content = {'custom': custom, 'id': id}
        return render(request, 'edit2.html', content)


def delete_customs(request, id):
    custom = Customs.objects.get(id=id)
    custom.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_customs")


# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            return redirect('home')
    else:
        form =UserForm()
    return render(request, 'registration.html', {'register_form': form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")

# def send_message(request):
#     send_mail('Web programming:Сабагы басталды','My content','200103462@sdu.edu.kz',['200103462@stu.sdu.edu.kz','nursultan031702@mail.ru','200103387@stu.sdu.edu.kz'],
#               fail_silently=False,html_message='<b>Хабарлама жиберилди</b>')
#     return render(request, 'successfull.html')

def send_message(request):
    email = EmailMessage('Hello','Body goes here','200103462@stu.sdu.edu.kz',['200103462@stu.sdu.edu.kz','nursultan031702@mail.ru'],
                         headers={'Message-ID': 'foo'},)

    email.attach_file(r'C:\Users\Админ\Pictures\tank.png')
    email.send(fail_silently=False)
    return render(request, 'successfull.html')