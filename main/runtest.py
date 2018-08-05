# coding:utf-8
import sys
sys.path.append("E:\\Python\\Test_framework\\ApiTest_Framework\\ApiTest_Framework")

from base.runmethod import RunMethod
from base.get_data import GetData
from util.common_util import CommonUtil
class RunTest():
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()

	# 程序执行
	def go_on_run(self):
		res = None
		rows_count = self.data.get_case_line()
		for i in range(1,rows_count):
			url = self.data.get_request_url(i)
			print (url)
			method = self.data.get_request_method(i)
			is_run = self.data.get_is_run(i)
			data = self.data.get_data_for_json(i)
			print (data)
			expect = self.data.get_expcet_data(i)
			# print (expect)
			header = self.data.is_header(i)
			if is_run:
				res = self.run_method.run_main(method,url,data,header)
				if self.com_util.is_contain(expect, res):
					self.data.write_result(i,'pass')
				else:
					self.data.write_result(i,'fail')
			print (res)

if __name__ == '__main__':
	run = RunTest()
	print(run.go_on_run())
