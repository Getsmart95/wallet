from __future__ import absolute_import, unicode_literals
from .celery import application
import requests

@app.task
def call_api():
    request = requests.get('https://api.github.com/events')