# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .main import read_opc_ua


# @shared_task
# def add(x, y):
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)


@shared_task
def read_server():
    read_opc_ua()
