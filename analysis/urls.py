from django.urls import path
from analysis import views

urlpatterns = [
    path('analyze/', views.analyze, name='analyze'),
]
