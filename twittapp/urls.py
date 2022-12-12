from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('home', views.home_view, name = 'home'),
    path('popular', views.popular_view, name = 'popular'),
    path('twitts', views.twitt_list_view, name = 'list'),
    path('twittit', views.twitt_create_view, name = 'create'),
    path('twitta', views.twitt_profile_view, name = 'profile'),

    #APIs
    path('api/twitts/<int:twitt_id>', views.twitt_detailed_view, name = 'detailed'),
    path('api/twitts/<int:twitt_id>/delete', views.twitt_delete_view, name = 'delete'),
    path('api/twitts/<int:twitt_id>/owner', views.twitt_owner_view, name = "getowner"),
    path('api/twitts/action', views.twitt_like_view, name = "twittaction"),
    path('api/profiles/<int:user_id>', views.twitt_profile_lookup_view, name = "profilelookup"),
]