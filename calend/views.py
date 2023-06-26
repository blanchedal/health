from django.shortcuts import render

# Create your views here.
def calend(request):
    return render(request, 'calend/no-sidebar.html')