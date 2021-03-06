from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user_app'
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name="user_app/login.html"), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page="user_app:index"), name='logout'),
  path('', views.index , name='index'),
]