from celery import shared_task
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

@shared_task(bind=True)
def test_task(self):
    logger.info(">>> CELERY WORKER: Starting test_task execution...")
    for i in range(10):
        logger.info(f">>> CELERY WORKER count: {i}")
        print(f">>> CELERY WORKER count: {i}", flush=True)
        time.sleep(1)
    logger.info(">>> CELERY WORKER: Finished test_task!")
    return "Done"

@shared_task
def test_connection_task():
    logger.info(">>> test_connection_task executed successfully!")
    return "Celery connection is successful!"

@shared_task
def long_running_task(duration=5):
    logger.info(f">>> Starting long_running_task for {duration} seconds...")
    time.sleep(duration)
    logger.info(f">>> Completed long_running_task after {duration} seconds.")
    return f"Task completed after {duration} seconds"