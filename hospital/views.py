from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'hospital/index.html')


def about(request):
    return render(request,'hospital/about.html')

def introduce(request):
    return render(request,'hospital/introduce.html')