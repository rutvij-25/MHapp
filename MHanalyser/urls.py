from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('takeatest/',views.takeatest,name='takeatest'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('login/',views.loginPage,name='login'),
    path('result/',views.result,name='result'),
    path('wrong/',views.wrong,name='wrong'),
    path('about/',views.about,name='about')
]