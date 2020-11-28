from django.urls import path

from .views import homePageView, addView, readPageView, writePageView, badReadView, searchView, userView, userView2

urlpatterns = [
    path('', homePageView, name='home'),
    path('read/', readPageView, name='read'),
    path('write/add/', addView, name='add'),
    path('write/', writePageView, name='write'),
    path('read/<int:user>/', badReadView, name='badRead'),
    path('search/', searchView, name='search'),
    path('user/', userView, name='user'),
    path('user2/', userView2, name='user2'),
]