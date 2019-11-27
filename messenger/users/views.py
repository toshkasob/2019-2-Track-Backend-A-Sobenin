from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from users.models import User

# Create your views here.
def user_profile(request, profile_id):
    if request.method == 'GET':
        try:
            print(f'профиль пользователя {profile_id}')
            #user_passport = User.objects.get(user_id=profile_id)
            return JsonResponse({'name': 'Anton', 'surname': 'Sobenin',
                'nickname': 'sav_kR0L1k', 'age': 25, 'profile_id': f'{profile_id}'
                })
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])

def user_contacts(request, profile_id):
    if request.method == 'GET':
        try:
            print(f'контакты пользователя {profile_id}')
            #user_friends = User.objects.get(user_id=profile_id)
            return JsonResponse({'ID': f'{profile_id}', 'name': 'Denis', 'surname': 'Denisov'})
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])

def search_user(request, name):
    if request.method =='GET':
        try:
            user_passport = User.objects.all()
            user_passport = user_passport.filter(name__contains=name)
        except:
            raise Http404
        return JsonResponse({'user_passport':f'{user_passport}'})
    else:
        return HttpResponseNotAllowed(['GET']) 
