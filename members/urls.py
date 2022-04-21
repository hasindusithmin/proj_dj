
from django.urls import path
from . import views
urlpatterns = [
    path('',views.root,name='app root'),
    path('all',views.get_member,name='return all members')
]