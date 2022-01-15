from random import randint
from django.http import request
from django.http import response
from django.shortcuts import redirect, render
from .models import Psychic
from datetime import datetime

psy1 = Psychic('Psychic - 1', randint(10, 99))
psy2 = Psychic('Psychic - 2', randint(10, 99))

def home(request):
    return render(request, 'edison/home.html')

def start(request):
    return render(request, 'edison/start.html')


def app(request):

    
    data = [{'psy_number': psy1.psy_number}, {'psy_number': psy2.psy_number}]

    if request.method == "POST":


        user_stat = {
                'user_num': request.POST.get('user_num'),
                'user_num_created_at': datetime.now(),
                'psy1_num': data[0]['psy_number'],
                'psy2_num': data[1]['psy_number']
                }

        psychic_stat = [{
            'title': i.title, 
            'attempt': i.attempt_set(),
            'credibility': i.credibility_set(request.POST.get('user_num'), i.psy_number),
            } for i in [psy1, psy2]]

        request.session['psychic_stat'] = psychic_stat

        psy1.psy_number = randint(10, 99)
        psy2.psy_number = randint(10, 99)
        
        try:
            request.session['user_stat'] += [user_stat]
        except Exception:
            request.session['user_stat'] = [user_stat]

 
        return redirect('/start')

    return render(request, 'edison/app.html', {'data': data})


def user_stat(request):
    try:
        data = request.session['user_stat']
    except Exception:
        data = ''

    return render(request, 'edison/user_stat.html', {'data': data})


def psychic_stat(request):
    try: 
        data = request.session['psychic_stat']
    except Exception:
        data = ''

    return render(request, 'edison/psychic_stat.html', {'data': data})