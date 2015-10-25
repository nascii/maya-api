# -*- coding: utf-8 -*-

import logging
from pyramid.config import Configurator
from iddybiddy.routes import configure
from iddybiddy.app import App

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    config = Configurator()
    wsgi_app = configure(config).make_wsgi_app()
    server = make_server(
        App.config.get("server", "host"),
        int(App.config.get("server", "port")),
        wsgi_app
    )

    logging.getLogger().info(
        "Started on {0}:{1}".format(
            App.config.get("server", "host"),
            App.config.get("server", "port"),
        )
    )
    server.serve_forever()
