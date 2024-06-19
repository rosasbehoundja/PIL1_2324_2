# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Discussion, Message
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.discussion_id = self.scope['url_route']['kwargs']['discussion_id']
        self.discussion_group_name = f'chat_{self.discussion_id}'

        # Rejoindre le groupe de discussion
        await self.channel_layer.group_add(
            self.discussion_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Quitter le groupe de discussion
        await self.channel_layer.group_discard(
            self.discussion_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope["user"].id

        discussion = await sync_to_async(Discussion.objects.get)(id=self.discussion_id)
        sender = await sync_to_async(User.objects.get)(id=user_id)

        new_message = await sync_to_async(Message.objects.create)(
            discussion=discussion,
            sender=sender,
            text=message
        )

        # Envoyer le message au groupe de discussion
        await self.channel_layer.group_send(
            self.discussion_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.email
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Envoyer le message au WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
