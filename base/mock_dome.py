# coding:utf-8

from mock import mock

#模拟mock的封装
def mock_test(mock_mothod,request_data,url,method,response_data):
	mock_mothod = mock.Mock(return_value=response_data)
	res = mock_mothod(url,method,request_data)
	return res
	
