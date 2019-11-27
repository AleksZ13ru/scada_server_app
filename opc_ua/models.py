from django.db import models
# from django.contrib.postgres.fields import JSONField
# from jsonfield import JSONField
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import json


class Server(models.Model):
    enable = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return '{0} | url={1}'.format(self.name, self.url)


class Tag(models.Model):
    enable = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    url = models.CharField(max_length=20)

    def server_name(self):
        return self.server.name

    def __str__(self):
        return '{0} = {1}/{2}'.format(self.name, self.server.name, self.url)


class Result(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.TextField(default='[]')
    status = models.TextField(default='[]')

    def tag_name(self):
        return self.tag.name

    def display_len(self):
        return '%d: %d' % (len(json.loads(self.value)), len(json.loads(self.status)))

    @staticmethod
    def add(tag, value=0, status=0):
        current_time = timezone.now().time()
        total_minute = (current_time.hour * 60 + current_time.minute)
        try:
            result_instance = Result.objects.get_or_create(tag=tag, date=timezone.now().date())[0]
            old_value = result_instance.value
            old_status = result_instance.status
            result_instance.value = Result.create_list(old_value, total_minute, value)
            result_instance.status = Result.create_list(old_status, total_minute, status)
            result_instance.save()

        except ObjectDoesNotExist:
            print("opc_ua_models_ObjectDoesNotExist")
            pass

    @staticmethod
    def create_list(old_list, full_length, value):
        my_list = json.loads(old_list)[:full_length]
        while len(my_list) < full_length:
            my_list.append(0)
        my_list.append(value)
        return json.dumps(my_list)
