from http.server import BaseHTTPRequestHandler
from datetime import datetime
import urllib.parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    print (self.path)
    s = self.path
    print(urllib.parse.parse_qs(s[2:]))
    print("-----------------")
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return
