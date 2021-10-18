
from asyncio.tasks import sleep
from channels import layers
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
from asgiref.sync import async_to_sync

class DataGenerator(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"

        await(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name,
        )
        await self.accept()
        await self.send(text_data=json.dumps({"status":"Connected!!!!!!"}))

    async def receive(self, text_data=None):
        pass

    async def disconnect(self, close_code):
        pass

    async def send_notification(self, event):
        print("consumer here ")
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload' : data}))