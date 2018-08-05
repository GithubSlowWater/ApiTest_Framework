# coding:utf-8
import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {
	'username':'zhishui',
	'password':'888888'
}


def send_post(url,data):
	res = requests.post(url=url, data=data).json()
	return json.dumps(res)
print (send_post(url,data))



# res = requests.post(url=url,data=data)
# print (res.text)
