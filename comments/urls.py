from django.urls import path
from comments import views

urlpatterns = [
    path('', views.comments, name='comments'),
]