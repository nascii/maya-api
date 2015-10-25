# -*- coding: utf-8 -*-


import logging
from pyramid.response import Response
from iddybiddy.metadata import SERVICE_BANNER
from iddybiddy.renderers import JSON
from iddybiddy import tasks
#from iddybiddy.types import JsonResponse
#from iddybiddy import helpers

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

BANNER = """Running on {0}.""".format(
    SERVICE_BANNER)


def index(request):
    return Response(BANNER)


def reddit_r(request):
    return tasks.reddit.r.delay(request.matchdict["name"]).get()


def configure(config):
    config.add_renderer("json", JSON())
    config.add_route("index", "/")
    config.add_view(index, route_name="index")

    config.add_route("reddit_r", "/api/reddit/r/{name}", request_method="GET")
    config.add_view(reddit_r, route_name="reddit_r", renderer="json")

    return config
