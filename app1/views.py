from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return HttpResponse('msd is great captain')
def virat(request):
    return HttpResponse('virat is a run machine')
