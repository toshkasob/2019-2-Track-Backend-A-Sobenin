# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from datetime import date, time, datetime

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')

def chat_list(request):
    if request.method == 'GET':
        try:
            chat_id =request.GET.get('chat_id')
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            raise Http404
        return JsonResponse({'chats': 'All'})
    else:
        return HttpResponseNotAllowed(['GET'])

def chat_page(request, pk):
    if request.method == 'GET':
        try:
            #chats_all = Chats.objects.get(id=chat_id)
            print(f'chat_page is {pk}')
            chat_id = request.GET.get('chat_id')
            current_time = str(datetime.today())
        except:
            return HttpResponseNotFound('No this chat')
        return JsonResponse({'idChat': pk, 'text': 'How a u?', 'time': current_time})
    else:
        return HttpResponseNotAllowed(['GET'])