import json
from django.core.serializers import serialize

class Ajax_handler():

    def send_id(self,id):
        context = { 'id' : id }
        context_serialized =  json.dumps(context)
        print(context_serialized)
        return context_serialized
