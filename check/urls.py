from django.urls import path
from .views import *

app_name = 'check'
urlpatterns = [
    path('', check, name='check'),
    path('preschool', preschool, name='preschool'),
    path('child', child, name='child'),
    path('preschool_result', preschool_result, name='preschool_result'),
    path('checkbmi', checkbmi, name='checkbmi'),
    path('createbmi', createbmi, name='createbmi'),
    path('bmiresult', bmiresult, name='bmiresult'),
    path('nqex', nqex, name='nqex'),
    path('youth', youth, name='youth'),
    path('adult', adult, name='adult'),
    path('oldman', oldman, name='oldman'),
]