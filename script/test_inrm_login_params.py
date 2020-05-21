# 导包
import unittest
import logging
import requests
from parameterized import parameterized

import app
from api.login_api import TestLoginApi
from utils import assert_common, read_login_data


# 创建测试类,继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = TestLoginApi()

    def tearDown(self):
        ...
    filename = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filename))
    def test01_login_success(self,case_name,jsonData,http_code,success,code,message):
        # 发送登录请求
        headers = {"Content-Type": "application/json"}
        jsonData = jsonData
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        # print("结果:", result)
        logging.info("结果: {}".format(result))
        # 使用封装的通用断言函数
        assert_common(http_code, success, code, message, response, self)
