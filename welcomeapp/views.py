from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome(request):
 res=HttpResponse("<http><body bgcolor=blue><h1><center>welcome to srikanthpage</center></h1></body></http>")
 return res