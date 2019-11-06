# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from datetime import date, time, datetime

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')

def chat_list(request):
    try:
        return JsonResponse({'chats': 'All'})
    except request.method != 'GET':
        raise HttpResponseForbidden

def chat_page(request, pk):
    try:
        print(f'chat_page is {pk}')
        current_time = str(datetime.today())
        return JsonResponse({'idChat': pk, 'text': 'How a u?', 'time': current_time})
    except request.method != 'GET':
        raise HttpResponseForbidden