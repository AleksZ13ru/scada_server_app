from __future__ import absolute_import
import sys
from opc_ua.models import Server, Tag, Result, MessageTag, MessageEvent
from opcua import Client

sys.path.insert(0, "..")


def read_opc_ua():
    servers = Server.objects.filter(enable=True)
    for server in servers:
        client = Client(server.url)
        try:
            client.connect()
            tags = Tag.objects.filter(enable=True)
            for tag in tags:
                var = client.get_node(tag.url)
                value = var.get_value()
                if type(value) == float:
                    value = round(value, 2)
                Result.add(tag=tag, value=value, status=1)
                print("{0} = {1}".format(tag.name, value))

            # message_events = MessageEvent.objects.filter(ask_dt=None)
            message_tags = MessageTag.objects.filter(enable=True)

            for tag in message_tags:
                var = client.get_node(tag.url)
                tag_value = var.get_value()

                # if tag_value != 0:
                i = 0
                for bit in format(tag_value, 'b').rjust(16, '0'):
                    if bit == '1':
                        MessageEvent.create(tag=tag, bit=i)
                        print(bit + ' - ' + str(i))
                    if bit == '0':
                        MessageEvent.ask(tag=tag, bit=i)
                    i += 1
                # if tag_value == 0:
                #     message_events = MessageEvent.objects.filter(ask_dt=None, bit__tag=tag)
                #     for message_event in message_events:
                #         message_event.ask()
                        # print('add code reset ask status!')

        finally:
            client.disconnect()
