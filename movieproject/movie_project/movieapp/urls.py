from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [
   path('',views.index,name='index.html'),
   path('movie/<int:movie_id>/',views.detail,name='detail'),
   path('addmovie' ,views.add_movie,name='add_movie'),
   path('update/<int:movie_id>/',views.update_movie,name='update_movie'),
   path('delete/<int:movie_id>/',views.delete_movie,name='delete_movie'),
]
