from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/ubuntu/music-api/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/music-api/access_log'
errorlog =  '/home/ubuntu/music-api/error_log'
