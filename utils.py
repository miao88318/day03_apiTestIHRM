import json
import app


# 通用断言函数
def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual(httpcode, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 定义读取登录数据的函数.并从外界接收文件名
def read_login_data(filename):
    # 使用内置函数open打开外界传入的文件名
    with open(filename, mode="r", encoding="utf-8")as f:
        # 使用内置模块json加载文件
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 4 读取每一组数据，并按照parameterized的要求，拼接数据成一个嵌套元组的形式
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
        # 打印结果,并return返回
        print(result_list)
    return result_list


# 1 定义读取员工模块数据的函数，并从外界接收数据文件路径和要读取的接口模块
def read_emp_data(filename,name):
    # 使用内置函数open打开外界传入的文件名
    with open(filename, mode="r", encoding="utf-8")as f:
        # 使用内置模块json加载文件
        jsonData = json.load(f)
        # 读取数据
        emp_data = jsonData.get(name)
        # 定义存放数据的空列表
        result_list = list()
        # 将数据转化为元组后添加到列表中
        result_list.append(tuple(emp_data.values()))
    # 5 打印结果，并return返回
    print(result_list)
    return result_list


if __name__ == '__main__':
    # filename = app.BASE_DIR + "/data/login_data.json"
    # print("路径为:", filename)
    # read_login_data(filename)
    filename = app.BASE_DIR + "/data/emp_data.json"
    read_emp_data(filename,"add_emp")  # 测试添加员工的数据
    read_emp_data(filename,"query_emp")  # 测试查询员工的数据
    read_emp_data(filename,"modify_emp")  # 测试修改员工的数据
    read_emp_data(filename,"delete_emp")   # 测试删除员工的数据