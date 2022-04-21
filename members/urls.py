
from django.urls import path
from . import views
urlpatterns = [
    path('',views.root,name='app root'),
    path('all',views.read,name='return all members'),
    path('one/<int:id>',views.read_one,name='return a memebers'),
    path('add',views.create,name='create a memeber'),
    path('edit/<int:id>',views.update,name='update a member')
]