from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),

    # 하나의 요청 --> 2개의 방식 (Get vs POST)
    path('writeMemo/', views.writeMemo),
]