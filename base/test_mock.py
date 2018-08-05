# coding:utf-8
import unittest
from test001 import RunMain
from HTMLTestRunner import HTMLTestRunner
import mock

class TestMethod(unittest.TestCase):

	# @classmethod
	# def setUpClass(cls):
	# 	print ('类执行之前的方法')

	# @classmethod
	# def tearDownClass(cls):
	# 	print ('类执行之后的方法')
		
	def setUp(self):
		print ('========Start======')
		self.run = RunMain()

	def tearDown(self):
		print ('=========END=======')

	def test_01(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507006626132',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd3ddd5efeb04aa591ec12',
			'tokent':'0b4c502ba647664be04dfedb32ad4f3d',
			'cid':'0'
		}
		self.res = run.run_main(url,'POST',data)
		print (res)

	def test_02(self):
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507006626132',
			'uid':'5249192',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd3ddd5efeb04aa591ec12',
			'tokent':'0b4c502ba647664be04dfedb32ad4f3d',
			'cid':'0'
		}
		mock_data = mock.Mock(return_value=data)
		self.res = RunMain.run_main(url,'POST',data)
		print (res)

if __name__ == '__main__':
	filepath = "../report/htmlreport.html"
	fp = file(filepath, 'wb')

	suite = unittest.TestSuite()
	suite.addTest(TestMethod('test_01'))
	suite.addTest(TestMethod('test_02'))
	runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='this is report')
	runner.run(suite)
	# unittest.TextTestRunner().run(suite)
