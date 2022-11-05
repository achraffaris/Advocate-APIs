from django.urls import path
from . import views


urlpatterns = [
    path('advocates/', views.AdvocatesAPIView.as_view()),
    path('advocates/<str:username>/', views.AdvocateDetailAPIView.as_view())
]