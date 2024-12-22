from django.urls import path,include
from . import views

urlpatterns = [

    #CRUD
    path("",views.InsertPageView ,name = "insertpage"),
    path("insert/",views.InsertData ,name = "insert"),
    path("showpage/",views.ShowPage ,name = "showpage"),
    path("delete/<int:pk>",views.DeleteData ,name = "delete"),
    path("registerpage/",views.RegisterPage ,name = "registerpage"),
    path("register/",views.UserRegister ,name = "register"),
    path("editpage/<int:pk>",views.Editpage ,name = "editpage"),
    path("update/<int:pk>",views.UpdateData ,name = "update"),

]