from http.server import BaseHTTPRequestHandler
from os.path import join
from urllib import parse
import random as rand
import json

class handler(BaseHTTPRequestHandler):

	def name_gen(self, key):
		key = key.lower()
		if key == 'male':
			first_names = 'male_first_names.txt'
		elif key == 'female':
			first_names = 'female_first_names.txt'

		last_names = 'last_names.txt'

		f = open(join('data', first_names), "r")
		first_names = f.read().split()

		f = open(join('data', last_names), "r")
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

		json_value = json.dumps(output, ensure_ascii = False)
		result = json.loads(json_value)
		self.wfile.write(result.encode('utf8'))
		return