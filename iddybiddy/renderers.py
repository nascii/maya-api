# -*- coding: utf-8 -*-


import json
from pyramid.renderers import JSON as PyramidJSON


def _json_serializer(*args, **kwargs):
    # Get rid of this CRAPY ascii, I love UTF-8
    kwargs["ensure_ascii"] = False
    return json.dumps(*args, **kwargs)


class JSON(PyramidJSON):

    def __init__(self, serializer=_json_serializer, **kwargs):
        super(JSON, self).__init__(serializer=serializer, **kwargs)
