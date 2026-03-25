from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/user/', views.register_user, name='register_user'),
    path('register/expert/', views.register_expert, name='register_expert'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expert/dashboard/', views.expert_dashboard, name='expert_dashboard'),
    path('request/post/', views.post_request, name='post_request'),
    path('request/<int:request_id>/accept/', views.accept_request, name='accept_request'),
    path('request/<int:request_id>/cancel/', views.cancel_request, name='cancel_request'),
    path('request/<int:request_id>/complete/', views.complete_request, name='complete_request'),
    path('request/<int:request_id>/rate/', views.rate_expert, name='rate_expert'),
]