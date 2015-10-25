# -*- coding: utf-8 -*-


from celery import Celery
import functools
import logging

from iddybiddy.app import App

logging.basicConfig(level=logging.WARN)

config = App.config
app = Celery(
    config.get("celery", "queue"),
    broker=config.get("celery", "broker"),
    backend=config.get("celery", "backend"),
    include=["iddybiddy.tasks"]
)

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=config.get("celery", "result_expires"),
)


def task_autoretry(*args_task, **kwargs_task):
    def real_decorator(func):
        @app.task(*args_task, **kwargs_task)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except kwargs_task.get("autoretry_on", Exception) as exc:
                return wrapper.retry(exc=exc)
        return wrapper
    return real_decorator

if __name__ == "__main__":
    app.start()
