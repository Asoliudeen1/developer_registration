from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('candidates/', views.Candidates, name='candidates'),
    path('candidate/<int:candidate_id>/', views.Candidate, name='candidate'),

    path('login/', views.Login, name='loginpage'),
    path('logout/', views.Logout, name='logout'),
]