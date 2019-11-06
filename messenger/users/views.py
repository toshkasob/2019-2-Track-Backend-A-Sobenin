from django.http import JsonResponse
from django.http import HttpResponseForbidden

# Create your views here.
def user_profile(request):
    try:
        return JsonResponse({'name': 'Anton', 'surname': 'Sobenin',
            'nickname': 'sav_kR0L1k', 'age': 25
            })
    except request.method != 'GET' or request.method != 'POST':
        raise HttpResponseForbidden
def user_contacts(request):
    try:
        return JsonResponse({'ID': 0, 'name': 'Denis', 'surname': 'Denisov'})
    except request.method != 'GET':
        raise HttpResponseForbidden
