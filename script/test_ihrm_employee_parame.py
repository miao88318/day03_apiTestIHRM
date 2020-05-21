# 导包
import logging
import unittest

from parameterized import parameterized

import app
from api.employee import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common, read_emp_data


# 创建测试类
class TestEmployee2(unittest.TestCase):

    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        self.emp_api = TestEmployeeApi()
        self.login_api = TestLoginApi()

    # 编写测试用例 先登录
    def test01_login(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("登录的结果为: {}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 保存headers到全局变量app.py中
        app.HEADERS = headers
        # 打印令牌
        logging.info("保存到全局变量app中的请求头: {}".format(headers))  # 打印令牌
    filename = app.BASE_DIR + "/data/emp_data.json"

    # 添加员工
    @parameterized.expand(read_emp_data(filename,"add_emp"))
    def test02_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_api.add_emp(app.HEADERS, username, mobile)
        logging.info("添加成功:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        # 保存emp_id到全局变量app.py中
        app.EMP_ID = emp_id
        assert_common(http_code, success, code, message, response, self)

    # 查询员工
    @parameterized.expand(read_emp_data(filename,"query_emp"))
    def test03_query_emp(self,http_code,success,code,message):
        # 发送查询员工的请求
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询成功:{}".format(response.json()))
        assert_common(http_code,success,code,message, response, self)

    # 修改员工
    @parameterized.expand(read_emp_data(filename,"modify_emp"))
    def test04_modify_emp(self,username,http_code,success,code,message):
        # 修改员工
        response = self.emp_api.modify_emp(app.EMP_ID, app.HEADERS, username)
        print("修改成功:", response.json())
        assert_common(http_code,success,code,message, response, self)

    # 删除员工
    @parameterized.expand(read_emp_data(filename,"delete_emp"))
    def test05_delete_emp(self,http_code,success,code,message):
        # 删除员工
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除成功:{}".format(response.json()))
        assert_common(http_code,success,code,message, response, self)

