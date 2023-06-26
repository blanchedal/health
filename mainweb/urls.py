from django.urls import path
from .views import *

app_name = 'mainweb'
urlpatterns = [
    path('', index, name='index'),
    path('home/', index, name='home'),
    path('rice/', popup01, name='popup01'),
    path('meat/', popup02, name='popup02'),
    path('vegetable/', popup03, name='popup03'),
    path('fruit/', popup04, name='popup04'),
    path('milk/', popup05, name='popup05'),
    path('water/', popup06, name='popup06'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]