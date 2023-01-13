from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_view,name='task_view'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('abctask/',views.task_listview.as_view(),name='abctask'),
    path('abcdetailtask/<int:pk>/',views.task_detailview.as_view(),name='abcdetailtask'),
    path('abcupdatetask/<int:pk>/', views.task_updateview.as_view(), name='abcupdatetask'),
    path('abcdeletetask/<int:pk>/', views.task_deleteview.as_view(), name='abcdeletetask')

]