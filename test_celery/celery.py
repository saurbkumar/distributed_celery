from __future__ import absolute_import
from celery import Celery
from kombu import Queue
broker_url = 'amqp://kgmcrbkn:JEWBpwC2KUnSahYN680d9lkpqr8eh62o@fish.rmq.cloudamqp.com/kgmcrbkn'
result_backend = 'amqp'
app = Celery('test_celery',
             broker=broker_url,
             backend=result_backend,
             include=['test_celery.tasks'])

## Optional configuration, see the application user guide.
#app.conf.update(
#    result_expires=3600,
#)

#if __name__ == '__main__':
#    app.start()