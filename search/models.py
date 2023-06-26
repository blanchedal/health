from django.db import models
from django.contrib.auth.models import User

class Calorie(models.Model):
    name = models.CharField(max_length=100)
    wei = models.CharField(max_length=20)
    cal = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    
    class Meta: # 연동된 DB의 food_cal테이블 이용 지정
        managed = False
        db_table = 'food_cal'
    
    def __str__(self):
        return self.name
     
    @classmethod # type(음식분류)필드의 중복값을 제거해주는 함수
    def get_type_choices(cls):
        return cls.objects.order_by('type').values_list('type', 'type').distinct()


class SearchHistory(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True)
    keyword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    selected_type = models.CharField(max_length=255, default='')

    class Meta: # 연동된 DB의 search_history 테이블 이용 지정
        db_table = 'search_history'
        ordering = ['-created_at']

    def __str__(self):
        return self.keyword