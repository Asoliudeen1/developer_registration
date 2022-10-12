from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('candidates/', views.Candidates, name='candidates'),
    path('candidate/<int:candidate_id>/', views.Candidate, name='candidate'),

    # EXPORT TO PDF
    path('<int:pk>/exporttopdf/', views.exportToPdf, name='exporttopdf'),
   # path('pdf/<int:pk>/', views.Pdf, name='pdf'),

    #Login and Logout
    path('login/', views.Login, name='loginpage'),
    path('logout/', views.Logout, name='logout'),
]