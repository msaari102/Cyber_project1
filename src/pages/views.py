from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message, Account
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# Create your views here.

@login_required
def homePageView(request):
    users = User.objects.exclude(pk=request.user.id)
    messages = Message.objects.filter(Q(source=request.user) | Q(target=request.user))
    return render(request, 'pages/index.html', {'msgs': messages, 'users': users})

@login_required 
def writePageView(request):
    users = User.objects.exclude(pk=request.user.id)
    messages = Message.objects.filter(Q(source=request.user) | Q(target=request.user))
    return render(request, 'pages/write.html', {'msgs': messages, 'users': users})

@login_required
def userView(request):
    target = User.objects.get(id=request.GET.get('user'))
    account = Account.objects.get(owner=target)
    return render(request, 'pages/user.html', {'user': target, "account" : account})
    
@login_required
def userView2(request):
    return redirect('/user/?user=' + str(request.user.id))   

def addView(request):
	target = User.objects.get(username=request.POST.get('to'))
	Message.objects.create(source=request.user, target=target, content=request.POST.get('content'))
	return redirect('/')

@login_required
def readPageView(request):
	messages = Message.objects.filter(Q(source=request.user) | Q(target=request.user))
	users = User.objects.exclude(pk=request.user.id)
	return render(request, 'pages/read.html', {'msgs': messages, 'users': users})

@login_required     
def badReadView(request, user):
    messages = Message.objects.filter(Q(source=user) | Q(target=user))
    users = User.objects.exclude(pk=request.user.id)
    return render(request, 'pages/read.html', {'msgs': messages, 'users': users})
    
@login_required    
def searchView(request):
    search = request.GET.get('search')
    if len(search) == 0:
        search = "\'i\'"
    userid = str(request.user.id)
    messages = Message.objects.raw('SELECT * FROM pages_message WHERE target_id = '+str(userid)+' AND content LIKE \'' + search + '\'')
    users = User.objects.exclude(pk=request.user.id)
    return render(request, 'pages/read.html', {'msgs': messages, 'users': users})
    
