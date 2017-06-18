#! /usr/nim/env python
# coding: utf-8
import sys
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from runtob import app

if __name__ == '__main__':
    port = 5000
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    httpServer = HTTPServer(WSGIContainer(app))
    httpServer.listen(port)
    IOLoop.instance().start()
