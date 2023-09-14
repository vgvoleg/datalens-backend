import multiprocessing
import os

# higher than the supposed default nginx default of 75 seconds
keepalive = 80
timeout = 90

log_config = "/src/gunicorn/gunicorn_logging.ini"
bind = "[::]:" + os.environ.get("GUNICORN_LISTEN_PORT", "8080")
max_requests = int(os.environ.get("GUNICORN_MAX_RQ", "5000"))
max_requests_jitter = int(os.environ.get("GUNICORN_MAX_RQ_JITTER", "500"))
worker_class = "aiohttp.GunicornWebWorker"
workers = int(os.environ.get("GUNICORN_WORKERS_COUNT", multiprocessing.cpu_count() * 2 + 1))
