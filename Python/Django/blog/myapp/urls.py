from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('blogify/',views.blogify_view,name='blogify'),
    path('register/',views.register,name='register'),
    path('new_post/',views.create_post,name='new_post'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
]