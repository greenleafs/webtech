# -*- coding: utf-8 -*-
"""QA application."""
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm


def home(request):
    """Home page view."""
    question_qs = Question.objects.new()
    paginator = Paginator(question_qs, 10)
    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions.html', {'questions': questions})


def popular(request):
    """Popular page view."""
    question_qs = Question.objects.popular()
    paginator = Paginator(question_qs, 10)
    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions.html', {'questions': questions})


def question(request, id):
    """Question page view."""
    try:
        question = Question.objects.get(pk=id)
        answers = Answer.objects.filter(question=question)
        context = {
            'question': question,
            'answers': answers,
            'form': AnswerForm()
        }

        return render(request, 'question.html', context)
    except Question.DoesNotExist:
        raise Http404()


def ask(request):
    """Ask form."""
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():

            params = {
                'title': form.cleaned_data['title'],
                'text': form.cleaned_data['text']
            }

            if request.user.is_authenticated():
                params.update({'author': request.user})

            question = Question(**params)
            question.save()

            return HttpResponseRedirect(
                reverse('question', kwargs={'id': question.id})
            )
    else:
        form = AskForm()

    context = {'form': form}
    return render(request, 'ask.html', context)


def answer(request):
    """Answer post form."""
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = form.question

            params = {
                'text': form.cleaned_data['text'],
                'question': question
            }

            if request.user.is_authenticated():
                params.update({'author': request.user})

            answer = Answer(**params)
            answer.save()

            return HttpResponseRedirect(
                reverse('question', kwargs={'id': question.id})
            )

    return HttpResponseRedirect(reverse('root', kwargs={}))


def signup(request):
    """Signup view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user = authenticate(username=user.username,
                                     password=form.cleaned_data['password'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('root', kwargs={}))
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_user(request):
    """Login view."""
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('root', kwargs={}))

    login_error_msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_user = authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if auth_user:
                login(request, auth_user)
                return HttpResponseRedirect(reverse('root', kwargs={}))
            else:
                login_error_msg = 'Login error'
    else:
        form = LoginForm()

    context = {
        'form': form,
        'error': login_error_msg
    }

    return render(request, 'login.html', context)


def logout_user(request):
    """Logout."""
    logout(request)
    return HttpResponseRedirect(reverse('root', kwargs={}))


def test(request, *args, **kwargs):
    """Test view."""
    return HttpResponse('OK')
