#coding:utf-8
import requests
import json
class RunMain:
   def __init__(self,url,method,data=None):
       self.res = self.run_main(url,method,data)

   def send_get(self,url,data):
       #requests.packages.urllib3.disable_warnings()
       res=requests.get(url=url,data=data).json()
       return res

   def send_post(self,url,data):
       requests.packages.urllib3.disable_warnings()
       res=requests.post(url=url,data=data).json()
       return res


   def run_main(self,url,method,data=None):
       res=None
       if method=='GET':
           res=self.send_get(url,data)
       else:
           res=self.send_post(url,data)
       return res
       
if __name__=='__main__':
  url = 'http://coding.imooc.com/api/cate'
  data = {
      'timestamp':'1507006626132',
      'uid':'5249191',
      'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
      'secrect':'078474b41dd3ddd5efeb04aa591ec12',
      'tokent':'0b4c502ba647664be04dfedb32ad4f3d',
      'cid':'0'
    }
  run = RunMain(url,'POST',data)
   #print(run.res)
  print(run.run_main(url,'POST',data))
