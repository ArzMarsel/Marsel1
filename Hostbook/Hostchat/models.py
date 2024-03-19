from django.db import models


class HostMessage(models.Model):
    author_name = models.TextField('Name:', max_length=15)
    author_email = models.TextField('Email:', blank=True)
    message_text = models.TextField('Text:')
    date_posted = models.DateField('Date:'), models.TimeField('Time:')


class ChatMessage(models.Model):
    author_name = models.TextField('Name:', max_length=15)
    author_email = models.TextField('Email:', blank=True)
    message_text = models.TextField('Text:')
    date_posted = models.DateField('Date:'), models.TimeField('Time:')

