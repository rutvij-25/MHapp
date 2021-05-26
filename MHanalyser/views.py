from django.shortcuts import redirect, render
from . import forms
from ML.predict import predict
# Create your views here.
ans = []
def home(request):
    return render(request,'MHanalyser/home.html')

def takeatest(request):
    global ans
    if(request.method) == 'POST':
        d = request.POST.dict()
        ans = list(d.values())[1:]
        ans = [int(i) for i in ans]
        if(len(ans)<40):
            return redirect('wrong')
        return redirect('result')

    return render(request,'MHanalyser/takeatest.html')


def wrong(request):
    return render(request,'MHanalyser/wrong.html')

def result(request):
    context = {'result':predict(ans)[0]}
    return render(request,'MHanalyser/result.html',context)


def about(request):
    return render(request,'MHanalyser/about.html')