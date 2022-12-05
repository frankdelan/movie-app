from django.urls import path
from .views import show_rating, create_rating, choose_movie

app_name = 'user_app'

urlpatterns = [
    path('rating', show_rating, name='rating_page'),
    path('rating/create', create_rating, name='create_page'),
    path('rating/choose', choose_movie, name='choose_page')
]