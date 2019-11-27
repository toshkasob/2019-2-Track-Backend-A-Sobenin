from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound

# Create your views here.
def user_profile(request):
    if request.method == 'GET':
        try:
            #user_passport = Users.objects.get()
            return JsonResponse({'name': 'Anton', 'surname': 'Sobenin',
                'nickname': 'sav_kR0L1k', 'age': 25
                })
        except:
            return HttpResponseNotFound()
    else:
        raise HttpResponseNotAllowed(['GET'])
def user_contacts(request):
    if request.method == 'GET':
        try:
            #user_passport = Users.objects.get()
            return JsonResponse({'ID': 0, 'name': 'Denis', 'surname': 'Denisov'})
        except:
            return HttpResponseNotFound()
    else:
        raise HttpResponseNotAllowed(['GET'])
