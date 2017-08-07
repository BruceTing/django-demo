from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms import formset_factory

import logging

from .forms import CommentForm, MyForm
from .models import Users, BigData

# Create your views here.
logger = logging.getLogger('common_logger')

def index(request):
    logger.info('you call index function...')
    # user = Users.objects.get(username='mazheng')
    # logging.info(user)
    # request.session['name'] = 'jack'
    # CommentFormSet = formset_factory(CommentForm)
    # if request.method == 'POST':
    #     formset = CommentFormSet(request.POST, request.FILES)
    #     if formset.is_valid():
    #         pass
    # else:
    #     formset = CommentFormSet()
    if request.method == 'POST':
        formset = CommentForm(request.POST)
        message = 'success'
        if formset.is_valid():
            checkBox_colors = formset.cleaned_data['favorite_colors']
            return HttpResponseRedirect('/demoapp/index1/')
    else:
        formset = CommentForm()
    return render(request, 'index.html', {'formset': formset})


def index1(request):
    form = MyForm(request.POST)
    # name = request.session['name']
    return render(request, 'index1.html', {'form': form})

def save_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        logger.info('user:{}, password:{}, email:{}'.format(username, password, email))
        user = Users(username=username, password=password)
        user.save(using='fdms')
        return HttpResponseRedirect('/demoapp/list/')
    return render(request, 'index2.html')

def save_data(request):
    if request.method == 'POST':
        source = request.POST['source']
        content = request.POST['content']
        by_who = request.POST['by_who']
        collect_date = request.POST['collect_date']
        logger.info('source:{}, content:{}, by_who:{}, collect_date:{}'.format(source, content, by_who, collect_date))
        data = BigData(source=source, content=content, by_who=by_who, collect_date=collect_date)
        data.save()
        return HttpResponseRedirect('/demoapp/list/')
    return render(request, 'index2.html')

def list(request):
    users = Users.objects.all()
    datas = BigData.objects.all()
    return render(request, 'index3.html', locals())

def test(request):
    data = {
        'name': 'jack'
    }
    # logger.info('the method is called, the data is {}'.format(data))
    return JsonResponse(data=data)

