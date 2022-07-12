from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime

def index(request):
    return render(request, 'view_count_app/index.html')

users = {}
def increment_count(request):
    print(users)
    session_id_number = request.COOKIES.get('session_id_number')
    session = users.get(session_id_number)
    if not session:
        session_id_number = str(random.randint(100000,999999))
        
        users[session_id_number] = {
            'count': 1,
            'start_time': datetime.datetime.now()
        }
    else:
        users[session_id_number]['count'] += 1
    response = render(request, 'view_count_app/index.html', users[session_id_number])
    response.set_cookie('session_id_number', session_id_number)
    return response