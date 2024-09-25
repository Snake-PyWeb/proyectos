from django .urls import path
from myapp import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("admin_panel/",views.admin_panel,name="admin_panel"),
]