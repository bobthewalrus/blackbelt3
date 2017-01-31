from django.shortcuts import render, HttpResponse, redirect
from models import User, Poke
from django.contrib import messages
from django.urls import reverse
from django.db.models import F

# Create your views here.


def index(request):

    return render(request, "login_registration/index.html")

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request,messages.INFO, message)

def loginvalidate(request):
    if request.method == "POST":
        print 'here'
        print request.POST['email']
        result = User.objects.loginvalidation(request.POST)
        print "Login validation complete"
        # print result

        if result[0] == False:
            print_messages(request, result[1])
            return redirect(reverse('index'))
        # print request
        print result[1]
        print "Passing to the login function"
        return login(request, result[1])
    else:
        print "Method's not even post for loginvalidate"
        return redirect('/')

def login(request, user):
    print "Here at Login"
    request.session['user'] = {
    'id': user.id,
    'name' : user.name,
    'alias' : user.alias,
    'email' : user.email,
    'pokecount' : user.pokecount,
    }
    return redirect('success')

def registervalidate(request):
    result= User.objects.registervalidation(request.POST)

    if not result[0]:
        print_messages(request, result[1])
        return redirect('/')

    return login(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect('/')
    distinctpokecount = Poke.objects.filter(pokeid=request.session['user']['id']).order_by('User__pokecount').values('user').distinct().count()
    distinctpokers = Poke.objects.filter(pokeid=request.session['user']['id'])
    pokecount=0
    for i in distinctpokers:
        print "top of list"
        print i.id
        print i.pokeid
        print i.user
        print "bottom of list"

            #  i.user.name == j.user.name
    allpokers = User.objects.exclude(id=request.session['user']['id'])
    # pokelist =


    context = {
    "listpokers":allpokers,
    "distinctpokecount":distinctpokecount,
    "distinctpokers":distinctpokers
    }


    return render(request, 'login_registration/success.html', context)

def addpoke(request, id):
    user = User.objects.get(id=request.session['user']['id'])
    print request.session['user']['id']
    print id
    addcount = User.objects.filter(id=id).update(pokecount = F('pokecount')+1)
    pokecount = User.objects.filter(id=request.session['user']['id']).values('pokecount')
    addpoke = Poke.objects.create(pokeid=id, user=user)


    return redirect('/success')

def logout(request):
    request.session.clear()
    # request.session.pop('user')
    return redirect('/')
