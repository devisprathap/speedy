from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
     path('form1',views.form1,name='form1'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('link',views.link,name='link'),
    path('submit',views.submit,name='submit'),




]
