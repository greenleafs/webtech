# -*- coding: utf-8 -*-
"""QA models."""

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class QuestionManager(models.Manager):

    """QuestionManager."""

    def new(self):
        """New method."""
        return self.all().order_by('-pk')

    def popular(self):
        """Popular method."""
        return self.all().order_by('-rating')


class Question(models.Model):

    """Question model."""

    title = models.CharField(max_length=255,
                             verbose_name=_('заголовок вопроса'))

    text = models.TextField(verbose_name=_('полный текст вопроса'))

    added_at = models.DateField(auto_now_add=True,
                                verbose_name=_('дата добавления вопроса'))

    rating = models.IntegerField(
        default=0,
        verbose_name=_('рейтинг вопроса (число)'))

    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               verbose_name=_('автор вопроса'))

    likes = models.ManyToManyField(
        User,
        verbose_name=_('список пользователей, поставивших "лайк"'),
        related_name='like_users')

    objects = QuestionManager()

    class Meta:

        """Meta."""

        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def get_absolute_url(self):
        """Return absolute url."""
        return "/question/%i/" % self.id


class Answer(models.Model):

    """Answer model."""

    text = models.TextField(verbose_name=_('текст ответа'))

    added_at = models.DateField(auto_now_add=True,
                                verbose_name=_('дата добавления ответа'))

    question = models.ForeignKey(
        Question,
        verbose_name=_('вопрос, к которому относится ответ'))

    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               verbose_name=_('автор ответа'))

    class Meta:

        """Meta."""

        verbose_name = "Answer"
        verbose_name_plural = "Answers"
