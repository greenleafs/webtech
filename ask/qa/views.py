# -*- coding: utf-8 -*-
"""QA application."""
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import Http404

from qa.models import Question, Answer


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
            'answers': answers
        }

        return render(request, 'question.html', context)
    except Question.DoesNotExist:
        raise Http404()


def test(request, *args, **kwargs):
    """Test view."""
    return HttpResponse('OK')
