from users.views import user_contacts, user_profile
from django.urls import path

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('profile/contacts/', user_contacts, name='user_contacts'),
]