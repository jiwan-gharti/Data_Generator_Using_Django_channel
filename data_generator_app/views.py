from channels.layers import get_channel_layer
from django.shortcuts import redirect, render
from .thread import CreateStudentThread
import json

# Create your views here.

async def home(request):

    for i in range(1,10):
        channel_layer = get_channel_layer()
        data = {'count': i}
        await(channel_layer.group_send)(
            'new_consumer_group',{
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
    return render(request, "home.html")


from django.http import JsonResponse
def generate_student_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        total = data.get("total")
        CreateStudentThread(int(total)).start()
        return JsonResponse({'status':"ok"})
