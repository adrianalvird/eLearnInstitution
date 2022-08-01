from django.shortcuts import render, HttpResponse

# Create your views here.

def support(request):
    return render(request,'support.html')
 
