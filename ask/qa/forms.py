# -*- coding: utf-8 -*-
"""QA application form."""
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _


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
