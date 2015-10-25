# -*- coding: utf-8 -*-


def convert_params(params):
    res = {}
    pairs = zip(params.keys(), params.values())
    for p in pairs:
        key, value = p
        if res.get(key, None) is None:
            res[key] = []
        res[key].append(value)

    return res
