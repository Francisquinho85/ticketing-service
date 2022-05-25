from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/egs/ticketing-service/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/egs/ticketing-service/access_log'
errorlog =  '/home/egs/ticketing-service/error_log'
