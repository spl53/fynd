''' Created by sachin on 01 Dec 2017'''

from django.conf.urls import url
from imdb import views

urlpatterns = [
	url(r'^search_movie/$',views.search_movie, name = 'search_movie'),
	url(r'^movies/$',views.movies, name = 'movies'),
]
