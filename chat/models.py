from django.db import models

class Message(models.Model):
    message_text = models.TextField('текст сообщения')
    message_author = models.CharField('автор сообщения', max_length = 50)
    message_time = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.message_text


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

