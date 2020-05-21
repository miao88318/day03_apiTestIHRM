# 导包
import unittest
# 创建测试套件
import HTMLTestRunner_PY3

import app
from script.test_ihrm_employee_parame import TestEmployee2
from script.test_inrm_login_params import TestIHRMLogin

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestEmployee2))
# 定义测试报告的名称
report_name = app.BASE_DIR + "/report/ihrm.html"
with open(report_name,"wb")as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="IHRM接口测试报告", description="人类资源管理")
    runner.run(suite)
print("测试一下")
print("在测试一下")

print("哈哈哈")
