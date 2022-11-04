from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.home, name='home'),
    path('details/<str:namee>', views.details, name='details'),
    path('show_register/',views.show_register, name="show_register"),
    # path('loginuser/',views.loginuser, name="loginuser"),
    # path('loginuser/loginuser',views.loginuser, name="loginuser"),
    path('show_register/register', views.register, name='register'),
    path('show_login/', views.show_login, name='show_login'),
    path('show_login/loginuser', views.loginuser, name='loginuser'),
    path('logout',views.logout,name="logout"),
    
]
