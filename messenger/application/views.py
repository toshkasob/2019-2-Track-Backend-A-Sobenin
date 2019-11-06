from django.shortcuts import render
from django.http import HttpResponseForbidden

def main_page(request):
    try:
        print('we have the main_page (render in application/view.py)')
        return render(request, 'index.html')
    except request.method != 'GET' or request.method != 'POST':
        raise HttpResponseForbidden