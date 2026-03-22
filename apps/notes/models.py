from django.db import models
from django.core.validators import MaxLengthValidator

class Notes(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', help_text='Введите заголовок заметки')
    content = models.TextField(validators=[MaxLengthValidator(1000)], verbose_name='Содержание', help_text='Введите текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at']

    def __str__(self):
        return self.title[:50]

