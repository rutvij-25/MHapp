from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('takeatest/',views.takeatest,name='takeatest'),
    path('result/',views.result,name='result'),
    path('wrong/',views.wrong,name='wrong'),
    path('about/',views.about,name='about')
]