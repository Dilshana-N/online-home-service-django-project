from django.urls import path
from ohs import views
urlpatterns = [

    path("", views.index, name="index"),
    path("login_page", views.login_page, name="login_page"),
    path("indexx", views.indexx, name="indexx"),
    path("registration", views.registration, name="registration"),
    path("regiworker", views.regiworker, name="regiworker"),
    path("dashboardcustomer", views.dashboardcustomer, name="dashboardcustomer"),
    path("dashboardworker", views.dashboardworker, name="dashboardworker"),
    path("customer_registration", views.customer_registration, name="customer_registration"),
    # path("customer", views.customer, name="customer"),
    path("workers", views.workers, name="workers")




    # path("logincu", views.logincu, name="logincu")

]
