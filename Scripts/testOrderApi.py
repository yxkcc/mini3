import logging

import pytest

from Api.apiFactory import ApiFactory
import utils


class TestOrderApi:

    def test_order_list_api(self):
        """订单列表"""
        res = ApiFactory.get_order_api().order_list_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言订单数量大于0
        assert len(res.json().get('data')) > 0
        # 断言包含关键字段
        assert False not in [i in res.text for i in ['id', 'order_no', 'create_time', 'total_price']]
        # 断言current_page的值
        assert res.json().get('current_page') == 1

    def test_create_order_api(self):
        """创建订单"""
        res = ApiFactory.get_order_api().create_order_api(12, 1)
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res, 200)
        # 断言包含关键字段
        assert False not in [i in res.text for i in ['order_id', 'order_no', 'create_time', 'pass']]
        # 断言pass的值为True
        assert res.json().get('pass') is True
        # 订单编号和订单id大于0
        assert len(res.json().get('order_no')) > 0 and len(res.json().get('order_id')) > 0

    def test_query_order_pai(self):
        """订单详情"""
        res = ApiFactory.get_order_api().query_order_pai(112)
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res, 200)
        # 断言包含关键字段
        assert False not in [i in res.text for i in ['id', 'order_no', 'snap_items', 'snap_name']]
        # 断言snap_items大于0
        assert len(res.json().get('snap_items')) > 0
        # 断言id
        assert res.json().get('id') == 112
        # 断言地址信息
        assert res.json().get('snap_address').get('name') == '肖肖'
        assert res.json().get('snap_address').get('mobile') == '13862812345'
