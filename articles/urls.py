from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new),
    path('create/', views.create),
    # Read
    path('', views.index),
    path('<int:question_id>/answers/create/', views.answer_create),
    # Delete
    path('<int:question_id>/delete/', views.delete),
]