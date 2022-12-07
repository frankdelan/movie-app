from django.urls import path
from .views import show_wishlist, add_movie, choose_movie

app_name = 'wishlist_app'

urlpatterns = [
    path('', show_wishlist, name='list_page'),
    path('add', add_movie, name='add_page'),
    path('choose', choose_movie, name='choose_page')
]