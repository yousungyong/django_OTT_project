from django.urls import path
from django.contrib.auth import views as auth_views
from acc import views

app_name='acc'
urlpatterns = [
    path('', views.no_login, name="no_login"),
    path('login/', auth_views.LoginView.as_view(template_name='acc/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
    path('signup/', views.signup, name='signup'),
]
