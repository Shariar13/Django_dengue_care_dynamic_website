from asyncio.windows_events import NULL
from tkinter import Y
from urllib.parse import quote
from django.db.models import fields
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse, request
from django.template import context
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
import joblib
import sklearn




def home(request):
    return render(request, "index.html")

def dengue (request):
    return render (request, "dengue-test.html")

def dengue_test (request):
    cls = joblib.load("f.sav")

    lis = []


    age = request.GET

    age = int(request.GET['age'])
    gender = int(request.GET['gender'])
    example1 = int(request.GET['example1'])
    example2 = int(request.GET['example2'])
    example3 = int(request.GET['example3'])
    example4 = int(request.GET['example4'])
    example5 = int(request.GET['example5'])
    example6 = int(request.GET['example6'])
    example7 = int(request.GET['example7'])
    example8 = int(request.GET['example8'])
    example9 = int(request.GET['example9'])
    example10 = int(request.GET['example10'])
    example11 = int(request.GET['example11'])
    example12 = int(request.GET['example12'])
    example13 = int(request.GET['example13'])
    example14 = int(request.GET['example14'])
    example15 = int(request.GET['example15'])
    example16 = int(request.GET['example16'])
    example17 = int(request.GET['example17'])
    example18 = int(request.GET['example18'])
    example19 = int(request.GET['example19'])
    example20 = int(request.GET['example20'])

    if age == 0:
        messages.error (request, 'Please Enter A Valid AGE')
        return render (request, "index.html")
    else:



        lis.append(age)
        lis.append(gender)
        lis.append(example1)
        lis.append(example2)
        lis.append(example3)
        lis.append(example4)
        lis.append(example5)
        lis.append(example6)
        lis.append(example7)
        lis.append(example8)
        lis.append(example9)
        lis.append(example10)
        lis.append(example11)
        lis.append(example12)
        lis.append(example13)
        lis.append(example14)
        lis.append(example15)
        lis.append(example16)
        lis.append(example17)
        lis.append(example18)
        lis.append(example19)
        lis.append(example20)


        ans = cls.predict([lis])

        if ans == 0:
            p_result = "আপনার ডেঙ্গু হয়েছে"
        elif ans == 1:
            p_result = "অভিনন্দন আপনার ডেঙ্গু হয় নাই"


        return render (request,"dengue-test.html",{"p_result":p_result})


