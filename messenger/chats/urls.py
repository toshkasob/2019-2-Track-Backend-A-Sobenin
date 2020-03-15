from chats.views import chat_list, chat_page, create_chat, new_chat
from chats.views import send_message, new_message
from django.urls import path, include

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:chat_id>/', chat_page, name='chat_page'),
    path('new_chat/create_chat/', create_chat, name='create_chat'),
    path('new_chat/', new_chat, name='new_chat'),
    path('<int:chat_id>/new_message/', new_message, name='new_message'),
    path('<int:chat_id>/new_message/send_message/', send_message, name='send_message'),
]