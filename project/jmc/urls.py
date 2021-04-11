from django.urls import path
from . import views

app_name = 'jmc'

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='students'),
    path('teacher/', views.teacher, name='teachers')
]