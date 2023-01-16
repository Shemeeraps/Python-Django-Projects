from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='index'),
     path('delete/<int:taskid>/',views.delete,name='delete'),
     path('update/<int:taskid>/',views.update,name='update'),
     path('classlistview/',views.todolistview.as_view(),name='classlistview'),
     path('classdetailview/<int:pk>', views.tododetailview.as_view(), name='classdetailview'),
     path('classupdateview/<int:pk>/',views.todoupdateview.as_view(),name='classupdateview'),
     path('classdeleteview/<int:pk>/',views.tododetailview.as_view(),name='classdeleteview'),
     ]