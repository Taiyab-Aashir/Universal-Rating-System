from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from polls import views
from polls.feed import Feeed
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_category/$', views.add_person, name='add_category'),
    url(r'^register/$', views.djangoregister, name='register'),
    url(r'^all_games/$', views.allgames),
    url(r'^add_book/$', views.add_book),
    url(r'^add_movie/$', views.add_movie),
    url(r'^login/$', views.djangologin),
    url(r'^logout/$', views.djangologout),
    url(r'^all_movies/$', views.allmovies),
    url(r'^all_books/$', views.allbooks),
    url(r'^add_game/$', views.add_game),
    url(r'^ajax_use/$', views.ajax_game, name='ajax-test-view'),
    url(r'^ajax_use2/$', views.ajax_book, name='ajax-test-view'),
    url(r'^ajax_use3/$', views.ajax_movies, name='ajax-test-view'),
    url(r'^comments/', Feeed()),
    url(r'^comment/', views.comment, name='comment')

]
