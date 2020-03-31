from django.urls import path
from ranking import views

urlpatterns = [
    path('analyze/', views.analyze, name='analyze'),
]
