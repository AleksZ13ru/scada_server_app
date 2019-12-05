from __future__ import absolute_import
import sys
from opc_ua.models import Server, Tag, Result, MessageTag, MessageEvent
from opcua import Client

sys.path.insert(0, "..")


def repack_word(word):
    # return (word[8:16]+word[0:8])[::-1]
    return word[::-1]


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

            message_tags = MessageTag.objects.filter(enable=True)

            for tag in message_tags:
                var = client.get_node(tag.url)
                tag_value = var.get_value()
                for idx, bit in enumerate(repack_word(format(tag_value, 'b').rjust(16, '0'))):
                    if bit == '1':
                        MessageEvent.create(tag=tag, bit=idx)
                        print(bit + ' - ' + str(i))
                    if bit == '0':
                        MessageEvent.ask(tag=tag, bit=idx)
                    i += 1
        finally:
            client.disconnect()
