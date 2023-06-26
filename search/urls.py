from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_calories, name='search_calories'),
    path('', views.search_calories_page, name='search_calories_page'),
    path('search_history/', views.search_history, name='search_history'), # 화면에 출력되는 함수가 아니라 실질적인 템플릿없어도 상관은 없지만 지정은 해주어야 함.
]