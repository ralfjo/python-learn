from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('createMemo/', views.createMemo),

    # 하나의 요청 --> 2개의 방식 (Get vs POST)
    path('writeMemo/', views.writeMemo),

    # 수정 페이지 요청
    path('edit/<str:idx>', views.editPage),

    # 수정 처리 DB
    path('edit/update/', views.updateMemo),

    # 삭제 처리 DB
    path('delete/<str:idx>', views.deleteMemo),
]