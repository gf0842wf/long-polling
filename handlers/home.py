# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import random
import time

class LongPollingHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        print self.request.arguments
        print repr(self.request.body)
        self.get_data(callback=self._over)
             
    def get_data(self, callback):
        if self.request.connection.stream.closed():
            return
        num = random.randint(1, 100)
        tornado.ioloop.IOLoop.instance().add_timeout(
            time.time()+3,
            lambda: callback(num)
        ) # 间隔3秒调用回调函数(模拟耗时,服务器没有数据更新就一直不调用finish关闭连接,这样就是长轮询)
             
    def _over(self, data):
        self.write(u"S==>B: %d" % data)
        self.finish() # 使用finish方法断开连接
    
    def get(self):
        self.render("long-polling.html")
        