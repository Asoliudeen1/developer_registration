from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('candidates/', views.Candidates, name='candidates'),
    path('<int:candidate_id>/', views.Candidate, name='candidate'),
    path('delete/<int:pk>/', views.Delete, name='delete'),


    #Login and Logout
    path('login/', views.Login, name='loginpage'),
    path('logout/', views.Logout, name='logout'),


    # EXPORT TO PDF
    path('<int:pk>/exporttopdf/', views.exportToPdf, name='exporttopdf'),
    path('pdf/<int:pk>/', views.pdf, name='pdf'),

    # SENDEMAIL
    path('email/', views.email, name='email'),

    #Chat 
    path('chat-candidate/<int:id>/', views.chat_candidate, name='chat-candidate')
]