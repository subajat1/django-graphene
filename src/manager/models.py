# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    user = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
