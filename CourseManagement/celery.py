from __future__ import absolute_import,unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CourseManagement.settings")
app = Celery("CourseManagement")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# Set the Redis URL for Celery to use as the message broker.
app.conf.broker_url = 'redis://red-cj6eai2cn0vc739mu980:6379/0'

# Set the result backend for Celery (Optional, but recommended)
# For example, using Redis as the result backend:
app.conf.result_backend = 'redis://red-cj6eai2cn0vc739mu980:6379/1'

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")