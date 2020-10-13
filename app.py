import logging.handlers
import os


def log_conf():
    """日志"""
    # 日志文件位置
    logPath = "./Log"
    # 声明日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 声明处理器 -控制台
    sh = logging.StreamHandler()
    # 声明处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logPath + os.sep + "mini.log",
                                                     when="midnight",
                                                     interval=1, backupCount=7,
                                                     encoding="utf-8")
    # 格式化字符串
    fmt = "%(asctime)s - %(levelname)s - [%(filename)s - %(funcName)s - %(lineno)d] - %(message)s"
    # 声明格式化器
    formatter = logging.Formatter(fmt)
    # 格式化器 添加到 处理器 -控制台
    sh.setFormatter(formatter)
    # 格式化器 添加到 处理器 -文件
    trfh.setFormatter(formatter)
    # 处理器 -控制台 添加到日志器
    logger.addHandler(sh)
    # 处理器 -文件 添加到日志器
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "001UFm000CFWrK1vx62004Drbx3UFm0o"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": ""
}


