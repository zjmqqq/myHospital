from django.shortcuts import render
from patient import models
# Create your views here.
def index(request):
    new_list = models.news.objects.all()[:4]
    return render(request,'hospital/index.html',{'new_list':new_list})


def about(request):
    return render(request,'hospital/about.html')

def introduce(request):
    return render(request,'hospital/introduce.html')