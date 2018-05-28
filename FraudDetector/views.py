from django.shortcuts import render
from django.http import HttpResponse
from .forms import UrlForm
def index(request):
    return render(request,'FraudDetector/index.html')

def get(self, request):
    form = UrlFrom()
    context = {
        "form":form
    }
    return render(request, 'FraudDetector/index.html', context)

def loading(request):
    return render(request,'FraudDetector/loading.html')

def results(request):
    return render(request,'FraudDetector/results.html')