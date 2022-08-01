from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')
 
def donators(request):
	return render(request,'donators.html')

def blueprint(request):
	return render(request,'blueprint.html')
