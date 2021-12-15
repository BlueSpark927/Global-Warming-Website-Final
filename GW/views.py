from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import activate
from numpy import positive

# Create your views here.
from .models import *


def index(request):
    return render(request, 'base/index.html')

def Graph1(request):
    return render(request, 'base/Graph1.html')

def Graph2(request):
    months = Months.objects.all()
    return render(request=request, template_name='base/Graph2.html',context={'months': months})




