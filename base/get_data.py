# coding: utf-8
import sys
sys.path.append("E:\\Python\\Test_framework\\ApiTest_Framework\\ApiTest_Framework")
from util.operation_excle import OpertionExcle
import data_config
from util.operation_json import OpertionJson

class GetData:
	def __init__(self):
		self.oper_excle = OpertionExcle()

	# 去获取excel行数，
	def get_case_line(self):
		return self.oper_excle.get_line()

	#获取是否执行
	def get_is_run(self,row):
		flag = None 
		col = int(data_config.get_run())
		run_model = self.oper_excle.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否有header
	def is_header(self,row):
		col = int(data_config.get_heard())
		header = self.oper_excle.get_cell_value(row,col)
		if header == 'yes':
			return data_config.get_header_value()
		else:
			return None

	# 获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.oper_excle.get_cell_value(row,col)
		return request_method

	# 获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.oper_excle.get_cell_value(row,col)
		return url

	# 获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.oper_excle.get_cell_value(row,col)
		if data == '':
			return None
		return data

	# 通过获取关键字拿到data的数据
	def get_data_for_json(self,row):
		opera_json = OpertionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	# 获取预期结果
	def get_expcet_data(self,row):
		col = int(data_config.get_expect())
		expect = self.oper_excle.get_cell_value(row,col)
		if expect == '':
			return None
		return expect

	# 写入数据
	def write_result(self,row,value):
		col = int(data_config.get_result())
		write_data = self.oper_excle.write_value(row,col,value)

	# 获取以来数据的key
	def get_depend_key(self,row):
		col = int(data_config.get_data_depend())
		depent_key = self.oper_excle.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key
    #判断是否有case的依赖
    def is_depend(self,row):
    	col = int(data_config.get_field_depend())
    	depend_case_id = self.oper_excle.get_cell_value(row,col)
    	if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(data_config.get_field_depend())
		data = self.oper_excle.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data