from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='class-view'),
    path('skills', views.skills, name='skills'),
    path('education', views.education, name='education')
]