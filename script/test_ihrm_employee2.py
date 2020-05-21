# 导包
import logging
import unittest
import app
from api.employee import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common


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
        logging.info("保存到全局变量app中的请求头: {}".format(app.HEADERS))  # 打印令牌

    # 添加员工
    def test02_add_emp(self):
        response = self.emp_api.add_emp(app.HEADERS, "哈哈8989", "13386561236")
        logging.info("添加成功:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        # 保存emp_id到全局变量app.py中
        app.EMP_ID = emp_id
        assert_common(200, True, 10000, "操作成功", response, self)

    # 查询员工
    def test03_query_emp(self):
        # 发送查询员工的请求
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询成功:{}".format(response.json()))
        assert_common(200, True, 10000, "操作成功", response, self)

    # 修改员工
    def test04_modify_emp(self):
        # 修改员工
        response = self.emp_api.modify_emp(app.EMP_ID, app.HEADERS, "小白555")
        print("修改成功:", response.json())
        assert_common(200, True, 10000, "操作成功", response, self)

    # 删除员工
    def test05_delete_emp(self):
        # 删除员工
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除成功:{}".format(response.json()))
        assert_common(200, True, 10000, "操作成功", response, self)
