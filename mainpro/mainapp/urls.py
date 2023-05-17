

from . import views
from django.urls import include, path

urlpatterns = [
     path('',views.demo,name='demo'), 
    #  path('add/',views.addition,name='addition'),
   # path('',views.home,name='home'),
#    path('about/',views.aboutpage,name='aboutpage'),
#    path('contacts/',views.contactspage,name='contactspage'),
]
