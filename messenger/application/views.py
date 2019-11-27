from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseNotFound

def main_page(request):
    if request.method == 'GET':
        try:
            print('we have the main_page (render in application/view.py)')
            return render(request, 'index.html')
        except:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotAllowed(['GET'])