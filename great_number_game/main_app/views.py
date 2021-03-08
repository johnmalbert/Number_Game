from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.
def index(request):
    request.session['answer'] = random.randint(1,100)
    print(request.session['answer'])
    request.session['counter'] = 0
    return render(request, "index.html")

def guess_lower(request):
    return render(request, "guess_lower.html")

def guess_higher(request):
    return render(request, "guess_higher.html")

def correct(request):
    return render(request, "correct.html")

def restart(request):
    print("restarting game")
    return redirect('/')

def guess(request):
    print(request.POST['user_guess'])
    request.session['guess'] = int(request.POST['user_guess'])
    print(f"User guess is now {request.session['guess']}")
    request.session['previous'] = request.session['guess']
    request.session['counter'] += 1
    print(request.session['counter'])
    context = {
        "previous" : request.session['previous'],
        "counter" : request.session['counter'],
        "answer" : request.session['answer']
    }
    if context['counter'] > 5 and request.session['guess'] != request.session['answer']:
        return render(request, "loser.html", context)
    if request.session['guess'] > request.session['answer']:
        return render(request, "guess_lower.html", context)
    elif request.session['guess'] < request.session['answer']:
        return render(request, "guess_higher.html", context)
    else:
        return render(request, "correct.html", context)

def leaders(request):
    print(request.POST['name'])
    print(request.session['counter'])
    context = {
        "name" : request.POST['name'],
        "score" : request.session['counter']
    }

    return render(request, "leaderboard.html", context)