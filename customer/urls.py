from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.start, name='start'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-up/', views.sign_up, name='signup'),
    path('home/', views.home, name='home'),
    path('add-post/', views.create_post, name='create_post'),

]
