from django.http import HttpResponse, JsonResponse
from .tasks import test_task, test_connection_task, long_running_task

# Create your views here.
def test_funcn(request):
    task = test_task.delay()
    return HttpResponse(f"Task dispatched to Celery! Task ID: {task.id}")

def test_connection_view(request):
    task = test_connection_task.delay()
    return JsonResponse({
        "status": "Connection test task dispatched to Celery",
        "task_id": task.id
    })

def long_running_view(request):
    duration = int(request.GET.get('duration', 5))
    task = long_running_task.delay(duration)
    return JsonResponse({
        "status": f"Long running task ({duration}s) dispatched to Celery",
        "task_id": task.id
    })
    
