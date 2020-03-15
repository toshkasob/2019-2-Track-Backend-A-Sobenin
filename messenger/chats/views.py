from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest
from datetime import date, time, datetime
from users.models import User
from chats.models import Chat
from members.models import Member
from message.models import Message
from chats.forms import ChatForm, SendMessageForm

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')
@csrf_exempt
@require_GET
def new_chat(request):
    if request.method == 'GET':
        try:
            print('we have the main_page (render in application/view.py)')
            return render(request, 'create_chat.html')
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
@require_GET
def new_message(request, chat_id):
    if request.method == 'GET':
        try:
            users = list(Member.objects.filter(chat_id=chat_id).values('id'))
            data = {
                "chat":chat_id,
                "user1": users,
                # "user2": users[1]
            }
            print('we have the main_page (render in application/view.py)')
            return render(request, 'send_message.html', context=data)
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
@require_GET
# def chat_list(request, profile_id):
def chat_list(request):
    # if request.method == 'GET':
        user_id = request.GET.get('user_id')
        chats_list = Chat.objects.filter(member__user_id=user_id).values(
            'id', 'topic', 'last_message', 'is_group_chat'
            )
        # возвращать не только id , но и остальн данные
        # all_my_chats = list(chats_list)
        print('получение своих чатов')
        return JsonResponse({'chats_list': list(chats_list)})
    # else:
    #     return HttpResponseNotAllowed(['GET'])

@csrf_exempt
@require_GET
def chat_page(request, chat_id):
    # if request.method == 'GET':
        print(f'chat_page is {chat_id}')
        try:
            messages = Message.objects.filter(chat_id=chat_id).values(
                'id', 'chat_id', 'user_id', 'content', 'added_at'
                ).order_by('-added_at')
            # chat = Chat.objects.get(id=chat_id)
            print(f'chat_page is {chat_id}')
            # получение чата 
        except Chat.DoesNotExist:
            return HttpResponseNotFound('No this chat')
        return JsonResponse({'idChat': chat_id, 'text': 'How a u?', 'test1':list(messages)}) # , 'time': current_time})
    # else:
    #     return HttpResponseNotAllowed(['GET'])

@csrf_exempt
@require_POST
def create_chat(request):
    # if "POST" == request.method:
        # form = ChatForm(request.POST)
        # if form.is_valid():
        #     chat = form.save()
        #     return JsonResponse({
        #         'msg': 'Создан новый чат',
        #         'id': chat.id,
        #     })
        # return JsonResponse({'errors': form.errors}, status=400)
        # создание чата

        form = ChatForm(request.POST)
        if form.is_valid():
            chat_id = form.save()
            return JsonResponse({'chat_id': chat_id})
        return JsonResponse({'errors': form.errors}, status=400)
        # user_id = request.POST.get('user_id', False)
        # if user_id is False:
        #     return HttpResponseBadRequest
        # # try:
        #     user = User.objects.get(id=user_id)
        # # except:
        # #     raise Http404
        # is_group_chat = request.POST.get('is_froup_chat', False)
        # topic = request.POST.get('topic')
        # chat = Chat.objects.Create(is_group_chat=is_group_chat, topic=topic)
        # member = Member.objects.Create(user=user, chat=chat, new_messages=0)
        # return JsonResponse({'chats_id': f'{chat_id} was created'})
    # else:
    #     return HttpResponseNotAllowed(['POST'])

@csrf_exempt
@require_POST
def send_message(request, chat_id):
    form = SendMessageForm(request.POST)
    if form.is_valid():
        message_id = form.save()
        return JsonResponse({'message_id': message_id})
    else:
        return JsonResponse({'errors': form.errors}, status=400)

