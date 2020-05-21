# 编写初始化日志的代码
# 导入app.py模块
import logging
import app
# 调用app.py中初始化日志的函数
app.init_logging()
# 打印日志 调式结果
logging.info("测试日志")