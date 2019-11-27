# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from datetime import date, time, datetime
from users.models import User
from chats.models import Chat

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')

def chat_list(request):
    if request.method == 'GET':
        try:
            print('получение своих чатов')
            # получение всех своих чатов
            # chats4owner = Chat.objects.all()
            # chats4owner = chats4owner.filter(user_id=)
        except : #Chat.DoesNotExist:
            raise Http404
        return JsonResponse({'chats': 'All'})
    else:
        return HttpResponseNotAllowed(['GET'])

def chat_page(request, chat_id):
    if request.method == 'GET':
        try:
            print(f'chat_page is {chat_id}')
            # получение чата 
        except:
            raise Http404 # HttpResponseNotFound('No this chat')
        return JsonResponse({'idChat': chat_id, 'text': 'How a u?', 'time': current_time})
    else:
        return HttpResponseNotAllowed(['GET'])