# -*- coding: utf-8 -*-

"""启动web server"""

import tornado.ioloop
import sys

from application import application

PORT = "8889"   

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
    application.listen(PORT)
    print "Development server is running at http://localhost:%s" % PORT
    print "Quit the server with CTRL-C"
    tornado.ioloop.IOLoop.instance().start()
