import logging

import requests, app


class OrderApi:
    def __init__(self):
        # 订单列表
        self.order_list_url = app.base_url + "/order/by_user"
        # 创建订单
        self.create_order_url = app.base_url + "/order"
        # 查看订单
        self.query_order_url = app.base_url + "/order/{}"

    def order_list_api(self, page=1):
        """
        订单列表
        :param page: 订单页数
        :return:
        """
        logging.info('订单-列表')
        # 参数
        data = {"page": page}
        logging.info('请求参数：{}'.format(data))
        return requests.get(self.order_list_url, params=data, headers=app.headers)

    def create_order_api(self, product_id, count):
        """
        创建订单
        :param product_id: 商品id
        :param count: 购买数量
        :return:
        """
        logging.info('订单-创建')
        # 参数
        data = {"products": [{"product_id": product_id, "count": count}]}
        logging.info('请求参数：{}'.format(data))
        # 返回响应结果
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_pai(self, order_id):
        """
        查看订单详情
        :param order_id: 订单id编号
        :return:
        """
        logging.info('订单-详情')
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
