from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from users.models import User
from members.models import Member
from chats.models import Chat
from django.db.models import Q

# Create your views here.
# def user_profile(request, profile_id):
def user_profile(request):
    if request.method == 'GET':
        # print(f'профиль пользователя {profile_id}')
        try:
            user_pasport = User.objects.filter(id=request.GET.get('user_id')).values(
                'id', 'first_name', 'nick', 'last_name', 'avatar'
                )
        except User.DoesNotExist:
            return HttpResponse(f'No such user with profile_id')

        return JsonResponse({'received_user_passport': list(user_pasport)})

        # try:
        #     print(f'профиль пользователя {profile_id}')
        #     #user_passport = User.objects.get(user_id=profile_id)
        #     return JsonResponse({'name': 'Anton', 'surname': 'Sobenin',
        #         'nickname': 'sav_kR0L1k', 'age': 25, 'profile_id': f'{profile_id}'
        #         })
        # except:
        #     return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])

def users_list(request):
    if request.method == 'GET':
        print('пользователи')
        try:
            found_users = User.objects.all().values('id', 'nick')
        except User.DoesNotExist:
            return HttpResponse(f'No any users ')
        return JsonResponse({'users':list(found_users)})
    else:
        return HttpResponseNotAllowed(['GET'])


# def user_contacts(request, profile_id):
#     if request.method == 'GET':
#         print(f'контакты пользователя {profile_id}')
#         try:
#             found_users = User.objects.all().values('id', 'nick')
#             # chats_by_user = Chat.objects.filter(id=Member.objects.filter(id=profile_id).values('id'))
#             # users_all = Member.objects.filter(chat=chats_by_user).values('id')
#             # found_users = User.objects.filter(id=users_all)
#         except User.DoesNotExist:
#             return HttpResponse(f'No any users for profile_id = {profile_id}')
#         return JsonResponse({'users':list(found_users), 'ID': profile_id})
#         # return JsonResponse({'ID': f'{profile_id}', 'name': 'Denis', 'surname': 'Denisov'})

#         # try:
#             # print(f'контакты пользователя {profile_id}')
#             # # user_friends = User.objects.get(user_id=profile_id)
#             # return JsonResponse({'ID': f'{profile_id}', 'name': 'Denis', 'surname': 'Denisov'})
#         # except:
#         #     return HttpResponseNotFound()
#     else:
#         return HttpResponseNotAllowed(['GET'])

def search_user(request):
    if request.method =='GET':
        request_param = 0
        data = request.GET
        name, surname, nick = data.get('name', ''), data.get('surname',''), data.get('nick','')
        try:
            # users_find_qs = User.objects.filter(
            users_found = list(
                User.objects.filter(
                    Q(first_name__icontains=name) 
                    | Q(last_name__icontains=surname)
                    | Q(nick__icontains=nick)
                    ).values('id', 'first_name', 'nick', 'last_name')
            )
            # users_found = list(users_find_qs)
        except User.DoesNotExist:
            return HttpResponse(f'No find any users with {request_param}')
        # user_passport = User.objects.all()
        # if flag == 1:
        #     user_passport = user_passport.filter(nick__contains=name)
        # else:
        #     user_passport = user_passport.filter(name__contains=name)
        # found_users = user_passport[:]

        # try:
            # user_passport = User.objects.all()
            # user_passport = user_passport.filter(name__contains=name)
        # except:
        #     raise Http404
        # return JsonResponse({'user_passport':f'{user_passport}'})
        return JsonResponse({'found_users': users_found})

    else:
        return HttpResponseNotAllowed(['GET']) 
