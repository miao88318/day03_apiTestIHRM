# 导包
import logging
import os
from logging import handlers
# 定义全局变量headers,提供给script中导入使用
HEADERS = None
# 定义全局变量headers,提供查询,修改,删除员工使用
EMP_ID = None
# 定义基础项目路径的变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 创建一个初始化日志的函数
def init_logging():
    # 在函数中创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器
    # 控制台处理器,将日志输出到控制台
    aw = logging.StreamHandler()
    # 文件处理器,将日志输出到文件当中
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="S", interval=5, backupCount=3, encoding="utf-8")
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    aw.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器当中
    logger.addHandler(aw)
    logger.addHandler(fh)
    # 在api模块下的__init__.py文件中进行初始化
