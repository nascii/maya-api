# -*- coding: utf-8 -*-


import requests
import logging

from iddybiddy.celery import task_autoretry
from iddybiddy.metadata import SERVICE_BANNER
from iddybiddy.types import TaskResponse

log = logging.getLogger("reddit")


@task_autoretry(max_retries=2, default_retry_delay=1)
def r(name):
    res = requests.get(
        "https://www.reddit.com/r/{0}.json".format(name), headers={"User-Agent": SERVICE_BANNER})

    return TaskResponse(data=res.json(), status_code=res.status_code)
