# 员工管理模块
# 导包
import unittest
import logging
import requests
from api.employee import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common


# 创建测试类,继承unittest.TestCase
class TestIHRMEmployee(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        self.emp_api = TestEmployeeApi()
        self.login_api = TestLoginApi()

    def tearDown(self):
        pass

    # def add_emp(self, headers,username, mobile):
    #     response = requests.post(self.emp_url,
    #                              json={
    #                                  "username": username,
    #                                  "mobile": mobile,
    #                                  "timeOfEntry": "2020-05-05",
    #                                  "formOfEmployment": 1,
    #                                  "workNumber": "123433",
    #                                  "departmentName": "测试部",
    #                                  "departmentId": "1063678149528784896",
    #                                  "correctionTime": "2020-05-17T16:00:00.000Z"
    #                              }, headers=headers)
    #     return response

    # 创建测试员工增删改查的函数
    def test01_employee_manage(self):
        # 实现员工的增删改查
        # 登录
        response = self.login_api.login({"mobile":"13800000002","password":"123456"},
                                        {"Content-Type": "application/json"})
        logging.info("登录的结果为: {}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("令牌: {}".format(headers))  # 打印令牌
        # 添加员工
        # response = requests.post(self.emp_url,
        #                          json={
        #                              "username": "小白166",
        #                              "mobile": "18800000033",
        #                              "timeOfEntry": "2020-05-05",
        #                              "formOfEmployment": 1,
        #                              "workNumber": "123433",
        #                              "departmentName": "测试部",
        #                              "departmentId": "1063678149528784896",
        #                              "correctionTime": "2020-05-17T16:00:00.000Z"
        #                          },headers=headers)
        # 添加员工
        # 添加员工
        # 添加员工
        response = self.emp_api.add_emp(headers, "小白666","13300000006")
        logging.info("添加成功:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        assert_common(200, True, 10000, "操作成功", response, self)

        # 查询员工
        # query_url = self.emp_url + "/" + emp_id
        # print("查询url:", query_url)
        # 发送查询员工的请求
        response = self.emp_api.query_emp(emp_id,headers)
        logging.info("查询成功:{}".format(response.json()))
        assert_common(200, True, 10000, "操作成功", response, self)

        # 修改员工
        # modify_url = self.emp_url + "/" + emp_id
        response = self.emp_api.modify_emp(emp_id,headers,"小白888")
        print("修改成功:", response.json())
        assert_common(200, True, 10000, "操作成功", response, self)

        # 删除员工
        # delete_url = self.emp_url + "/" + emp_id
        response = self.emp_api.delete_emp(emp_id,headers)
        logging.info("删除成功:{}".format(response.json()))
        assert_common(200, True, 10000, "操作成功", response, self)
