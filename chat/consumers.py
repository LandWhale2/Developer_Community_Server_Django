from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import Message, Room, RoomMessage
from chat.serializers import MeSerial, MessageSerializer
import logging
import re
import json



log = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print(self.room_name)
        print(self.room_group_name)

        try:
            room = Room.objects.get(label = self.room_group_name)
        except Room.DoesNotExist:
            print('DoesNotExist')
            room = Room(label = self.room_group_name)
            room.save()

        print(room)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        # handle = text_data_json['handle']
        room = Room.objects.get(label = self.room_group_name)

        if set(text_data_json.keys())!=set(('handle', 'message')):
            log.debug('예기치못한 포멧  = %s', text_data_json)
            return

        if text_data_json:
            log.debug('chat room : %s handle: %s message %s',
            room.label, text_data_json['handle'],text_data_json['message'])
            m = room.messages.create(**text_data_json)


        # Send message to room group
    
        await self.channel_layer.group_send(
            self.room_group_name,
            {'text':json.dumps(m.as_dict())}
        )

    # @database_sync_to_async
    # def getmessage(self):
    #     print(Message.objects.all()[0])
    #     return Message.objects.all()[0]

    # Receive message from room group
    # async def chat_message(self, event):
    #     message = event['message']
    #     handle = event['handle']
    #     timestamp = event['timestamp']

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message,
    #         'handle' : handle,
    #         'timestamp': timestamp,
    #     }))