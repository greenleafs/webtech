# -*- coding: utf-8 -*-
"""QA application."""
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


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

            question = Question(title=form.cleaned_data['title'],
                                text=form.cleaned_data['text'])
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
            answer = Answer(text=form.cleaned_data['text'],
                            question=question)
            answer.save()

            return HttpResponseRedirect(
                reverse('question', kwargs={'id': question.id})
            )

    return HttpResponseRedirect(reverse('root', kwargs={}))


def test(request, *args, **kwargs):
    """Test view."""
    return HttpResponse('OK')
