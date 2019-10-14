from django.db import models

class Message(models.Model):
    message_text = models.TextField('текст сообщения')
    message_author = models.CharField('автор сообщения', max_length = 50)
    message_time = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.message_text

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)  # Call the "real" save() method.
        new_message = None


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

