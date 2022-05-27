from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    return render(request,'home.html')

def quiz(request):
    if request.method == 'POST':
        myVar1 = request.POST.get("q1")
        myVar2 = request.POST.get("q2")
        myVar3 = request.POST.get("q3")
        myVar4 = request.POST.get("q4")
        myVar5 = request.POST.get("q5")
        score = 0
        if(myVar1 == "GuidovanRossum"):
         score += 1
        if(myVar2 == "no"):
         score += 1
        if(myVar3 == ".py"):
         score += 1
        if(myVar4 == "Pythoncodeisneithercompilednorinterpreted"):
         score += 1
        if(myVar5 == "Indentation"):
         score += 1
        per = (score*100)/5
        context = {
            'score': score,
            'per':per,
        }
        return render(request,'result.html',context)
    else:   
      return render(request,'quiz.html')

def result(request):
    return render(request,'result.html',context)


