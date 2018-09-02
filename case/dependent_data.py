#coding: utf-8
import sys
sys.path.append("E:\\Python\\Test_framework\\ApiTest_Framework\\ApiTest_Framework")

from util.operation_excle import OpertionExcle
from base.runmethod import RunMethod
from case.get_data import GetData
from jsonpath_rw import jsonpath,parse

class DependdentData:
	def __init__(self, case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()
		
	'''
	通过case_id获取该case的内容
	'''
	def get_case_line_data(self):
		rows_data = self.opera_excel.get_rows_data(self.case_id)
		return rows_data

	# 执行依赖测试，获取结果
	def run_dependent(self):
		run_method = RunMethod()
		row = self.opera_excel.get_rows_data(self.case_id)
		request_data = self.data.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row)
		url = self.data.get_request_url(row)
		run_method.run_main(method,url,request_data,header)
		return res

	# 根据依赖的key去获取执行依赖测试case的响应，然后返回
	def get_data_for_key(self,row):
		depend_data = self.data.get_depend_key(row)
		response_data = self.run_dependent()
		json_exe = parse(depend_data)
		madle = json_exe.find(response_data)
		return [math.value for math in madle][0]

		