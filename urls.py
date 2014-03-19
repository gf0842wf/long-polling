# -*- coding: utf-8 -*-

from handlers.home import LongPollingHandler

urls = [
    (r"/longpolling", LongPollingHandler),
    ]

