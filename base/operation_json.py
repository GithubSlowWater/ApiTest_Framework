# coding:utf-8
import json

# fp = open('../case/login.json')
# data = json.load(fp)
# print (data['login'])

class OpertionJson:

	def __init__(self):
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open('../case/login.json') as fp:
			data = json.load(fp)
			return data

	def get_data(self,id):
		return self.data[id]

if __name__ == '__main__':
	opjson = OpertionJson()
	print (opjson.get_data('login'))

