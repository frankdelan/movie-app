from django.urls import path
from .views import login_user, register_user, logout_user

app_name = 'user_app'

urlpatterns = [
    path('register/', register_user, name='register_page'),
    path('login/', login_user, name='login_page'),
    path('logout/', logout_user, name='logout'),
]
