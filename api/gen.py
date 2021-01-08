from http.server import BaseHTTPRequestHandler
from os.path import join
from urllib import parse
import random
import json

MALE_FIRST_NAMES_FILE_PATH = 'data/male_first_names.txt'
FEMALE_FIRST_NAMES_FILE_PATH = 'data/female_first_names.txt'
LAST_NAMES_FILE_PATH = 'data/last_names.txt'
MALE_KEY = 'male'

class handler(BaseHTTPRequestHandler):

	def read_file(self, file_name):
		try:
			f = open(file_name, "r")
			return f.read().split()
		except:
  			print("Error")
		finally:
			f.close()

	def random_name(self, list):
		return random.choice(list)

	def name_gen(self, key):
		first_names_file_path = MALE_FIRST_NAMES_FILE_PATH if key == MALE_KEY else FEMALE_FIRST_NAMES_FILE_PATH
		last_names_file_path = LAST_NAMES_FILE_PATH

		first_names = self.read_file(first_names_file_path)
		last_names = self.read_file(last_names_file_path)

		return "{first_name} {last_name}".format(first_name = self.random_name(first_names), last_name = self.random_name(last_names))

	def do_GET(self):
		dic = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

		if "gender" in dic:
			self.send_response(200)
			key = dic["gender"].lower()
			data = {key: self.name_gen(key)}
		else:
			self.send_response(404)
			data = {"error": "param missing"}

		self.send_header('Content-type','application/json; charset=utf-8')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

		data = json.dumps(data, ensure_ascii = False)
		json_value = json.dumps(data, ensure_ascii = False)
		result = json.loads(json_value)
		self.wfile.write(result.encode('utf8'))
		return