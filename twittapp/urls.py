from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('home', views.home_view, name = 'home'),
    path('twitts', views.twitt_list_view, name = 'list'),
    path('twitts/<int:twitt_id>', views.twitt_detailed_view, name = 'detailed'),
    path('twittit', views.twitt_create_view, name = 'create'),

    #APIs
    path('<int:twitt_id>/delete', views.twitt_delete_view, name = 'delete'),
    path('action', views.twitt_like_view, name = "twittaction"),
]