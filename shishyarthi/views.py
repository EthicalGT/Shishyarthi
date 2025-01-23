from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse

def homepage(req):
    return render(req,"index.html")