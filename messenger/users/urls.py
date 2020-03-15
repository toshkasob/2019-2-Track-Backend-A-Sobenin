from users.views import users_list, user_profile, search_user
from django.urls import path

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('contacts/', users_list, name='users_list'),
    path('search_users/', search_user, name='search_users'),
]