# coding:utf-8
import sys
sys.path.append("E:\\Python\\Test_framework\\ApiTest_Framework\\ApiTest_Framework")
import xlrd
from xlutils.copy import copy

class OpertionExcle:
	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id
			self.data = self.get_data()
		else:
			self.file_name = '../case/test01.xls'
			self.sheet_id = 0
		self.data = self.get_data()


	def get_data(self,):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	def get_line(self):
		tables = self.data
		return tables.nrows

	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	# 写入数据
	def write_value(self,row,col,value):
		'''
			写入excel数据
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)



if __name__ == '__main__':
	opers = OpertionExcle()
	print (opers.get_line())
	print (opers.get_cell_value(1,2))