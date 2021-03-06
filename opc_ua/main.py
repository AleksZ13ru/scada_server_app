from __future__ import absolute_import

import socket
import sys
from opc_ua.models import Server, Tag, Result, ResultOneMinute, MessageTag, MessageEvent
from opcua import Client

sys.path.insert(0, "..")


def repack_word(tag_value):
    # return (word[8:16]+word[0:8])[::-1]
    word = format(tag_value, 'b').rjust(16, '0')
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
                ResultOneMinute.add(tag=tag, value=value, status=1)
                print("{0} = {1}".format(tag.name, value))

            message_tags = MessageTag.objects.filter(enable=True)

            for tag in message_tags:
                var = client.get_node(tag.url)
                tag_value = var.get_value()
                for idx, bit in enumerate(repack_word(tag_value)):
                    if bit == '1':
                        MessageEvent.create(tag=tag, bit=idx)
                        print(bit + ' - ' + str(idx))
                    if bit == '0':
                        MessageEvent.ask(tag=tag, bit=idx)
        except AttributeError:
            pass
        except socket.error as err:
            print(err.args)
        else:
            client.disconnect()
        finally:
            pass
            # client.disconnect()
