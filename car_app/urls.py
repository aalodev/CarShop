from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPosition.as_view()),
    path('<int:pk>/', views.DetailPosition.as_view()),
    path('color/', views.ListColor.as_view()),
    path('color/<int:pk>/', views.DetailColor.as_view()),
    path('marka/', views.ListMarka.as_view()),
    path('marka/<int:pk>/', views.DetailMarka.as_view()),
    path('salon/', views.ListSalon.as_view()),
    path('salon/<int:pk>/', views.DetailSalon.as_view()),
]
