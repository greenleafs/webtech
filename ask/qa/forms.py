# -*- coding: utf-8 -*-
"""QA application form."""
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from qa.models import Question


class AskForm(forms.Form):

    """Ask form."""

    title = forms.CharField(label=_(u'Заголовок'),
                            max_length=255,
                            required=True)

    text = forms.CharField(
        label=_(u'Текст вопроса'),
        max_length=2048,
        required=True,
        widget=forms.Textarea())


class AnswerForm(forms.Form):

    """Answer form."""

    text = forms.CharField(
        label=_(u'Текст ответа'),
        max_length=2048,
        required=True,
        widget=forms.Textarea())

    question = forms.IntegerField(
        label=_(u'Номер вопроса'),
        required=True
    )

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.question = None

    def clean(self):
        """Clean form."""
        super(AnswerForm, self).clean()
        if not self.errors:
            entered_question = self.cleaned_data['question']

            try:
                self.question = Question.objects.get(pk=entered_question)
            except Question.DoesNotExist:
                raise ValidationError(
                    _('Unknown question %d') % entered_question
                )

        return self.cleaned_data


class SignupForm(forms.Form):

    """Signup form."""

    username = forms.CharField(
        label=_(u'Логин'),
        max_length=30,
        required=True
    )

    email = forms.EmailField(
        label=(u'Email'),
        max_length=30,
        required=True
    )

    password = forms.CharField(
        label=_(u'Пароль'),
        required=True,
        widget=forms.PasswordInput()
    )

    def clean(self):
        """Clean form."""
        super(SignupForm, self).clean()
        if not self.errors:
            username = self.cleaned_data['username']
            try:
                User.objects.get(username=username)
                raise ValidationError(
                    _('User with username "%s" already registered') % username
                )
            except User.DoesNotExist:
                pass

        return self.cleaned_data

    def save(self):
        """Create user."""
        params = {
            'username': self.cleaned_data['username'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password']
        }
        user = User.objects.create_user(**params)
        user.save()
        return user


class LoginForm(forms.Form):

    """Login form."""

    username = forms.CharField(
        label=_(u'Логин'),
        max_length=30,
        required=True
    )

    password = forms.CharField(
        label=_(u'Пароль'),
        required=True,
        widget=forms.PasswordInput()
    )
