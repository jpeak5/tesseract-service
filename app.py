#!/usr/bin/env python
import logging
import pprint
try:
    from urllib.parse import quote
except ImportError:
    # Python 2.
    from urllib import quote

import tornado.httpserver
import tornado.ioloop
import tornado.web
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body>Send us a file!<br/><form enctype="multipart/form-data" action="/" method="post">'
                   '<input type="file" name="the_file">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    # def post(self):
    #     self.set_header("Content-Type", "text/plain")
    #     self.write("yo")

    def post(self):
        for field_name, files in self.request.files.items():
            for info in files:
                filename, content_type = info["filename"], info["content_type"]
                body = info["body"]
                imgpath = '/tmp/'+filename
                tmpFile = open(imgpath, 'wb')
                tmpFile.write(body)
                out = pytesseract.image_to_pdf_or_hocr(Image.open(imgpath), extension='hocr')
                # out = pytesseract.image_to_string(Image.open(imgpath))
                self.write(out)
        self.write("OK")
        # self.write("You sent a file with name " + self.request.files.items()[0][1][0]['filename'] )
        # make a "memory file" using StringIO, open with PIL and send to tesseract for OCR
        # self.write(image_to_string(Image.open(StringIO.StringIO(self.request.files.items()[0][1][0]['body']))))

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
