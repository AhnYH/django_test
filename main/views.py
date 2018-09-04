# -*- coding: utf-8 -*-
from .forms import LoginForm
import sys
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as dlogin
from django.http import JsonResponse


@csrf_exempt
def login(request):
    form = LoginForm(request.POST or None)
    aaaaa = form.is_valid()
    if request.method == 'POST' and form.is_valid():
        user = form.authenticate_user()
        dlogin(request, user)
        sign = request.session

        return render(request, 'signin.html')


@csrf_exempt
def signin(request):
    return render(request, 'signin.html')


@csrf_exempt
def req_test(request):

    return JsonResponse({'msg': 'connect'})
