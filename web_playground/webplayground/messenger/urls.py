from django.urls import path 
from .views import ThreadList, ThreadDeatail


messenger_patterns = ([
    path('',ThreadList.as_view(),name='list'),
    path('thread/<int:pk>',ThreadDeatail.as_view(),name='detail'),
    ],"messenger")