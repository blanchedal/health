from django.shortcuts import render, redirect
from .forms import CreateBmi
from .models import Bmi

# Create your views here.
def check(request):
    return render(request, 'check/right-sidebar.html')

def preschool(request):
    return render(request, 'check/preschool_survey.html')

def child(request):
    return render(request, 'check/child_survey.html')

def preschool_result(request):
    return render(request, 'check/preschool_result.html')

def youth(request):
    return render(request, 'check/youth_survey.html')

def adult(request):
    return render(request, 'check/adult_survey.html')

def oldman(request):
    return render(request, 'check/oldman_survey.html')

def checkbmi(request):
    return render(request, 'check/health_check_bmi_index.html')

def createbmi(request):
    if request.method == 'POST':
        form=CreateBmi(request.POST)

        if form.is_valid():
            form.save()
            return redirect('bmiresult')
        else:
            return redirect('checkbmi')
    else:
        form = CreateBmi()

    return render(request,'check/health_check_createbmi.html',{'form':form})

def bmiresult(request):
    if request.method == 'POST':
        form = CreateBmi(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bmi_value = round(weight / ((height / 100) ** 2), 2)
            if bmi_value < 18.5:
                level = '저체중'
            elif bmi_value < 23:
                level = '정상'
            elif bmi_value < 25:
                level = '과체중'
            elif bmi_value < 30:
                level = '경도비만'
            elif bmi_value < 35:
                level = '중등도비만'
            else:
                level = '고도비만'
            bmi = Bmi.objects.create(name=name, height=height,weight=weight, user_bmi=bmi_value, level=level)
            return render(request, 'check/health_check_bmiresult.html', {'bmi': bmi})
    else:
        form = CreateBmi()
    return render(request, 'check/health_check_bmiresult.html', {'form': form})

def nqex(request):
    return render(request, 'check/nqex.html')
