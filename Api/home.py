import logging

import requests
import app


class HomeApi:
    """首页接口方法"""

    def __init__(self):
        # 轮播图
        self.banner_url = app.base_url + "/banner/{}"
        # 获取专题栏
        self.theme_url = app.base_url + "/theme"
        # 获取最近新品
        self.product_recent_url = app.base_url + "/product/recent"

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播图页面数
        :return: 响应对象
        """
        logging.info("首页-轮播图")
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids="1,2,3"):
        """
        获取专题栏位
        :param ids: 专题栏数据
        :return:响应对象
        """
        logging.info("首页-专题栏")
        data = {"ids": ids}
        logging.info("请求参数：{}".format(data))
        return requests.get(self.theme_url, params=data)

    def product_recent_api(self):
        """
        获取最近新品
        :return:响应对象
        """
        logging.info("首页-最近新品")
        return requests.get(self.product_recent_url)
