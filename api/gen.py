from http.server import BaseHTTPRequestHandler
import json
import random as rand
from urllib import parse

class handler(BaseHTTPRequestHandler):

	def name_gen(self, key):
		key = key.lower()
		if key == 'male':
			first_names = 'api/male_first_names.txt'
		elif key == 'female':
			first_names = 'api/female_first_names.txt'

		last_names = 'api/last_names.txt'

		f = open(str(first_names), "r")
		first_names = f.read().split()

		f = open(str(last_names), "r")
		last_names = f.read().split()

		first_names_size = len(first_names)
		last_names_size = len(last_names)
		first_index = rand.randint(0, first_names_size)
		last_index = rand.randint(0, last_names_size)

		name = first_names[first_index]+" "+last_names[last_index]
		output = {key : name}

		return json.dumps(output, ensure_ascii=False)

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

		if "gender" in dic:
			self.send_response(200)
			output = self.name_gen(dic["gender"])
		else:
			self.send_response(404)
			data = {}
			data['error'] = 'param missing'
			output = json.dumps(data)

		self.send_header('Content-type','application/json; charset=utf-8')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

		json_value = json.dumps(output, ensure_ascii = False)
		result = json.loads(json_value)
		self.wfile.write(result.encode('utf8'))
		return