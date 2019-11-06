from chats.views import chat_list
from django.urls import path

urlpatterns = [
    path('<int:pk>/<str:bla>/', chat_list, name='chat_list'),
]