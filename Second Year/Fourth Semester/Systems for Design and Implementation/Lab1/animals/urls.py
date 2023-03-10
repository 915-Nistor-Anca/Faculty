from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from animals import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view()),
    path('animals/<int:pk>/', views.AnimalDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)