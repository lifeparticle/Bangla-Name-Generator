from http.server import BaseHTTPRequestHandler
import json
import random as rand
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def name_gen(self,key):
          key=key.lower()
          if key=='male':
            first_names ='api/male_first_names.txt'
            last_names='api/last_names.txt'
          elif key=='female':
            first_names='api/female_first_names.txt'
            last_names='api/last_names.txt'

          f = open(str(first_names), "r")
          first_names=f.read().split()
          #print(first_names)
          f = open(str(last_names), "r")
          last_names=f.read().split()
          #print(last_names)
          length1=len(first_names)
          length2=len(last_names)
          first_index=rand.randint(0,length1)
          last_index=rand.randint(0,length2)

          name = first_names[first_index]+" "+last_names[last_index]
          output= {key:name}
          print(output)
          json1=json.dumps(output,ensure_ascii=False)
          #d = json.loads(json1)

          return json1
    
    def do_GET(self):
        s = self.path
        gen = parse_qs(urlparse(s).query)['gender'][0]
        print(gen, type(gen))
        self.send_response(200)
        self.send_header('Content-type','application/json; charset=utf-8')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        #s=parse_qs(urlparse(s).query)['gender'][0]
        #gen = list(gen)
        #gen=gen[0]
        output= self.name_gen(gen)
        json1=json.dumps(output,ensure_ascii=False)
        message=json.loads(json1)
        self.wfile.write(message.encode('utf8'))
        return