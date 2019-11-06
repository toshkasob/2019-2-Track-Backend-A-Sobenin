# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# def chat_list(request, pk, bla=None):
#     print(pk, bla)
#     return render(request, 'chat_list.html')

def chat_list(request, pk, bla=None):
    print(pk, bla)
    return JsonResponse({'test': 'App'})