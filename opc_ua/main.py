from __future__ import absolute_import
import sys
from opc_ua.models import Server, Tag, Result
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
        finally:
            client.disconnect()
