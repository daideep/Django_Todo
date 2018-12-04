
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addtodo, name='add'),
    path('complete/<t_id>', views.complete, name='complete'),
    path('deletecomplete', views.deletecomplete, name='deletecompleted'),
    path('deleteall', views.deleteall, name='deleteall'),
]
