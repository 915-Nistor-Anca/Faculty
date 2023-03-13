from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from animals import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view()),
    path('animals/<int:pk>/', views.AnimalDetail.as_view()),

    path('species/', views.SpecieList.as_view()),
    path('species/<int:pk>/', views.SpecieDetail.as_view()), #

    path('areas/', views.AreaList.as_view()),
    path('areas/<int:pk>/', views.AreaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)