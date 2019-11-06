from chats.views import chat_list, chat_page
from django.urls import path

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:pk>/', chat_page, name='chat_page'),
]