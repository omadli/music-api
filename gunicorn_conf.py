from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/<YOUR_PATH>/music-api/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/<YOUR_PATH>/music-api/access_log'
errorlog =  '/<YOUR_PATH>/music-api/error_log'
