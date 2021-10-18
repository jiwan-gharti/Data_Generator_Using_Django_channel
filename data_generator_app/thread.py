

from random import randint
from asgiref.sync import async_to_sync
import threading
from channels.layers import get_channel_layer
from .models import Student
import random
import time
import json
from faker import Faker


fake = Faker()

class CreateStudentThread(threading.Thread):

    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    
    def run(self):
        try:
            print("Thread execution start")
            channel_layer = get_channel_layer()
            current_total = 0

            for i in range(self.total):
                current_total += 1
                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,50)
                )
                
                data ={
                    "id": current_total,
                    "current_total":current_total,
                    "total":self.total,
                    "student_name":student_obj.student_name,
                    "student_email":student_obj.student_email,
                    "student_address":student_obj.address,
                    "student_age":student_obj.age
                }

                # print(data)
                async_to_sync(channel_layer.group_send)(
                    'new_consumer_group',{
                        'type'  : 'send_notification',
                        'value' : json.dumps(data)
                    }
                )
                time.sleep(1)                
        except Exception as e:
            print(e)

