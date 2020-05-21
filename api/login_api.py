# 导包
import requests


# 创建api测试类
class TestLoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    # 创建登录函数
    def login(self, jsonData, headers):
        # headers = {"Content-Type": "application/json"}
        # jsonData = {"mobile": "13800000002", "password": "123456"}
        response = requests.post(url=self.login_url, json=jsonData, headers=headers)
        return response
