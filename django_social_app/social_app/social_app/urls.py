
# social_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('user/all/', views.get_users, name="users-list"),
    path('user/id/', views.get_user_by_id, name="users-details"),
    path('user/search/', views.search_user_by_mobile, name="search-user"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),

]