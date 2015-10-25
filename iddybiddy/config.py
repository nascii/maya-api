# -*- coding: utf-8 -*-


import os
import codecs
from abc import ABCMeta, abstractmethod
from configparser import ConfigParser


class Provider(object, metaclass=ABCMeta):

    @abstractmethod
    def get(self, identity):
        return NotImplemented


class FSProvider(Provider):

    def get(self, identity):
        if not os.path.exists(identity):
            return None

        return codecs.open(identity, 'r', 'utf-8').read()


class Loader(object):

    def __init__(self, paths, filename, Provider=FSProvider):
        self.filename = filename
        self.provider = Provider()
        self._config = self._merge(self.load_configs(paths))

    def load_configs(self, paths):
        for path in paths:
            config_part = self.provider.get(os.path.join(path, self.filename))
            if config_part is None:
                continue

            yield self.parse_config(config_part)

    def _merge(self, configs):
        res = {}
        for config in configs:
            for section, content in config.items():
                if section not in res:
                    res[section] = {}
                res[section].update(content)

        return res

    def parse_config(self, s):
        config = ConfigParser()
        config.read_string(s)

        sections = config.sections()
        config_dict = {}
        for section in sections:
            items = config.items(section)
            config_dict[section] = {key: value for key, value in items}

        return config_dict

    def has_section(self, section):
        return section in self._config

    def dict(self):
        return self._config

    def get(self, section, key, default=None):
        return self._config.get(section, {}).get(key, default)
