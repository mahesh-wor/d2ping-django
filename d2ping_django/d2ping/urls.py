from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
        path('',views.index,name='index'),
        path('checkping',views.checkping,name='check-ping'),
        path('d2ping/checkping',views.checkping,name='ping-check')
]
