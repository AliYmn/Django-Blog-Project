from django.shortcuts import render
from .models import Category
# Create your views here.


def hello(request):
    nodes = Category.objects.all()
    return render(request,'test.html',locals())