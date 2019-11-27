from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Note(models.Model):
    STATUS_CHOICES = [
        ('ok', 'Завершено'),
        ('wr', 'В работе'),
    ]
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)
    datetime_start = models.DateTimeField()
    # datetime_stop = models.DateTimeField(blank=True)
    # status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='wr')
    text = models.TextField()

    # create_user = # todo: привязать к модели пользователей django
    # create_datetime = models.DateTimeField()

    def __str__(self):
        if len(self.text) > 20:
            return self.text[0:20] + ' ...'
        return self.text
