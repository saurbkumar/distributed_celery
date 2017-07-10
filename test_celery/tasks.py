from __future__ import absolute_import, unicode_literals
import time
from .celery import app

@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time task finished')
    return x + y    