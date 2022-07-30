from django.urls import path
from .import views

urlpatterns=[
    path('',views.Quizzes,name="Quizzes"),
    path('api/get-quiz/' , views.get_quiz,name="get-quiz")
]