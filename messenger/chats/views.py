# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest
from datetime import date, time, datetime
from users.models import User
from chats.models import Chat
from chats.models import Member

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')

def chat_list(request, profile_id):
    if request.method == 'GET':
        try:
            print('получение своих чатов')
            # получение всех своих чатов
            chats4owner = Chat.objects.all()
            chats4owner = chats4owner.filter(user_id=profile_id)
        except : #Chat.DoesNotExist:
            raise Http404
        return JsonResponse({'chats': f'All for {profile_id}'})
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

def create_personal_chat(request):
    if request.method == 'POST':
        # создание чата
        user_id = request.POST.get('user_id', False)
        if user_id is False:
            return HttpResponseBadRequest
        try:
            user = User.objects.get(id=user_id)
        except:
            raise Http404
        is_group_chat = request.POST.get('is_froup_chat', False)
        topic = request.POST.get('topic')
        chat = Chat.objects.Create(is_group_chat=is_group_chat, topic=topic)
        member = Member.objects.Create(user=user, chat=chat, new_messages=0)
        return JsonResponse({'chats_id': f'{chat_id} was created'})
    else:
        return HttpResponseNotAllowed(['POST'])