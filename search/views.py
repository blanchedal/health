from django.shortcuts import render
from django.http import JsonResponse
from .models import Calorie, SearchHistory

# 음식정보 통합검색 함수(검색바)
def search_calories(request):
    query = request.GET.get('query')
    type = request.GET.get('type')
    
    calories = Calorie.objects.filter(name__icontains=query)
    
    if type:
        calories = calories.filter(type=type)
    results = [{'name': cal.name, 'wei': cal.wei, 'cal': cal.cal} for cal in calories]

    #JSON형태로 반환
    return JsonResponse({'results': results})

# 카테고리 검색 드롭박스 보여지는 함수, search_calories 템플릿을 렌더링함
def search_calories_page(request):
    types = Calorie.get_type_choices()
    return render(request, 'search/search_calories.html', {'types': types})


# 사용자 검색기록 DB에 저장하는 함수 
def search_history(request):
    keyword = request.GET.get('keyword')
    selected_type = request.GET.get('selected_type')
    user = request.user if request.user.is_authenticated else None
    ip_address = request.META.get('REMOTE_ADDR')

    if keyword or selected_type: # 검색하거나 카테고리 선택 둘 중 하나만 해도 저장됨
        search_history = SearchHistory.objects.create(
            user=user,
            ip_address=ip_address,
            selected_type=selected_type,
            keyword=keyword
        )
        search_history.save() #저장만