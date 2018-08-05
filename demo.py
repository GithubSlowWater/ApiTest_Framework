# coding:utf-8
import requests
import json

# url = 'http://127.0.0.1:8000/login/'
# data = {
# 	'username':'zhishui',
# 	'password':'888888'
# }

url = 'http://coding.imooc.com/api/cate'
data = {
			'timestamp':'1507006626132',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd3ddd5efeb04aa591ec12',
			'tokent':'0b4c502ba647664be04dfedb32ad4f3d',
			'cid':'0'
}

def send_post(url,data):
	res = requests.post(url=url, data=data).json()
	return json.dumps(res)
print (send_post(url,data))



# res = requests.post(url=url,data=data)
# print (res.text)