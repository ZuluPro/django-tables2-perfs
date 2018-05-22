from django.urls import path
from core import views

urlpatterns = [
    path('table/', views.WithTablePaginationList.as_view()),
    path('django/', views.WithDjangoPaginationList.as_view()),
]
