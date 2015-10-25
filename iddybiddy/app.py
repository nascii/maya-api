# -*- coding: utf-8 -*-


import os
import logging
from iddybiddy.singleton import Singleton
from iddybiddy.config import Loader as ConfigLoader

__file_dir__ = os.path.dirname(os.path.abspath(__file__))
CONFIG_NAME = "app.ini"
DEFAULT_LOG_LEVEL = "WARN"
VERSION = open(os.path.join(__file_dir__, "VERSION")).read()
CONFIG_PATHS = [
    "{0}/config/{1}".format(os.getcwd(), env)
    for env in ["base", os.environ.get("ENV", "development")]
]

config = ConfigLoader(CONFIG_PATHS, CONFIG_NAME)
logging.basicConfig()
log = logging.getLogger()
log.setLevel(
    getattr(logging, config.get("global", "log_level", DEFAULT_LOG_LEVEL)))


class App(object, metaclass=Singleton):

    """Main application entrypoint"""

    __version__ = VERSION
    config = config
