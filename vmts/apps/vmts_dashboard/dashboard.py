# -*- coding: utf-8 -*-

import os

import tornado.web
import tornado.ioloop
import tornado.httpserver

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Vmts environment had not be initialized.')

from urls import urls

config = cfg.get_module('vmts_apps')


def run():
    """
    vmts dashboard entrance function.
    :return: None
    """

    settings = config.dashboard.settings
    app = tornado.web.Application(
        handlers=urls,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=config.dashboard.debug,
        **settings
    )

    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(config.dashboard.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
