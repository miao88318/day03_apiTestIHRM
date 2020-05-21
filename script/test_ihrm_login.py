# 登录管理模块
# 先用设计模式实现ihrm登录
# 根据设计模式的实现,封装ihrm登录接口
# 根据封装的接口,优化ihrm登录的代码
# 导包
import unittest
import logging
import requests
from api.login_api import TestLoginApi
from utils import assert_common


# 创建测试类,继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        # self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.login_api = TestLoginApi()

    def tearDown(self):
        ...

    # def login(self,jsonData,headers):
    #     # headers = {"Content-Type": "application/json"}
    #     # jsonData = {"mobile": "13800000002", "password": "123456"}
    #     response = requests.post(url=self.login_url, json=jsonData, headers=headers)
    #     return response

    def test01_login_success(self):
        # 发送登录请求
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        # print("结果:", result)
        logging.info("结果: {}".format(result))
        # 断言登录的结果
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, result.get("success"))
        # self.assertEqual(10000, result.get("code"))
        # self.assertIn("操作成功", result.get("message"))
        # 使用封装的通用断言函数
        assert_common(200, True, 10000, "操作成功", response, self)

    # 用户不存在
    def test02_mobile_is_not(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13802200002", "password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 密码错误
    def test03_password_is_error(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "error"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 账号为空
    def test04_mobile_is_empty(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "", "password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 密码为空
    def test05_password_is_empty(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": ""}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 手机号有特殊字符
    def test06_mobile_has_special(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "1380@000002", "password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 多参
    def test07_more_params(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002", "password": "123456", "more": "1"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, True, 10000, "操作成功", response, self)

    # 少参—mobile
    def test08_less_mobile(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 少参—password
    def test09_less_password(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mobile": "13800000002"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 无参
    def test10_none_params(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 参数写错—mboile
    def test11_error_params(self):
        headers = {"Content-Type": "application/json"}
        jsonData = {"mboile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 20001, "用户名或密码错误", response, self)

    # 传入None
    def test12_None(self):
        headers = {"Content-Type": "application/json"}
        jsonData = None
        response = self.login_api.login(jsonData, headers)
        result = response.json()
        logging.info("结果: {}".format(result))
        assert_common(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response, self)
