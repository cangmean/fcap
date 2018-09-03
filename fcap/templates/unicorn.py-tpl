import multiprocessing
import gevent.monkey
gevent.monkey.patch_all()

bind = '127.0.0.1:5000'

workers = 2

worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'