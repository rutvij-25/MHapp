from django.shortcuts import redirect, render
from .forms import *
from ML.predict import predict
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import *
import json
from .models import *

# Create your views here.


def home(request):
    return render(request,'MHanalyser/home.html')

@login_required(login_url='login')
def takeatest(request):

    if(request.method == 'POST'):
        d = request.POST.dict()
        ques = list(d.values())[1:]
        ques = [int(i) for i in ques]
        if(len(ques)<40):
            return redirect('wrong')
        else:
            ans = predict(ques)
            current_user = User.objects.get(username = request.user)
            data = UserModel.objects.get(user = current_user)
            data.result = ans
            data.answers = json.dumps(ques)
            data.save()
            return redirect('result')

    else:
        return render(request,'MHanalyser/takeatest.html')

@login_required(login_url='login')
def wrong(request):
    return render(request,'MHanalyser/wrong.html')

@login_required(login_url='login')
def result(request):
    print(request.user)
    current_user = User.objects.get(username = request.user)
    data = UserModel.objects.get(user = current_user)
    context = {'result':data.result}
    return render(request,'MHanalyser/result.html',context)

def about(request):
    return render(request,'MHanalyser/about.html')

@UnauthenticatedUser
def register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {user}')
            return redirect('login')
        
    context = {'form':form}
    return render(request,'MHanalyser/register.html',context)

@UnauthenticatedUser
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Incorrect Username or Password')
            return redirect('login')
    context = {}
    return render(request,'MHanalyser/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')