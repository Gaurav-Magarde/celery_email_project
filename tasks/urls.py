from django.urls import path
from .views import test_funcn, test_connection_view, long_running_view

urlpatterns = [
    path('', test_funcn, name='test_task'),
    path('test-connection/', test_connection_view, name='test_connection'),
    path('long-running/', long_running_view, name='long_running'),
]