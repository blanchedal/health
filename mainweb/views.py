from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainweb/index.html')

def popup01(request):
    return render(request, 'mainweb/popup01.html')

def popup02(request):
    return render(request, 'mainweb/popup02.html')

def popup03(request):
    return render(request, 'mainweb/popup03.html')

def popup04(request):
    return render(request, 'mainweb/popup04.html')

def popup05(request):
    return render(request, 'mainweb/popup05.html')

def popup06(request):
    return render(request, 'mainweb/popup06.html')

def signup(request):
    return render(request, 'mainweb/signup.html')

def login(request):
    return render(request, 'mainweb/login.html')