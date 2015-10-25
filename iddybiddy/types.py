# -*- coding: utf-8 -*-


class JsonResponse(object):

    def __init__(self, data, status_code=200):
        self._data = data
        self._status_code = status_code

    def __json__(self, request):
        request.response.status_code = self._status_code
        return {"response": self._data}


class TaskResponse(JsonResponse):

    def get_data(self):
        return self._data
