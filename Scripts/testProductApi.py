import logging

import utils
from Api.apiFactory import ApiFactory
import pytest


class TestProductApi:
    """商品接口测试类"""

    def test_product_classify_api(self):
        """
        商品分类
        :return:
        """
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言分类列表大于0
        assert len(res.json()) > 0
        # 断言包含关键字
        assert False not in [i in res.text for i in ['id', 'name', 'topic_img_id', 'update_time', 'img']]

    def test_classify_product_api(self):
        """
        分类下商品
        :return:
        """
        res = ApiFactory.get_product_api().classify_product_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言商品数量大于0
        assert len(res.json()) > 0
        # 断言包含关键字
        assert False not in [i in res.text for i in ['id', 'name', 'price', 'stock', 'main_img_url']]

    def test_product_detail_api(self):
        """

        :return:
        """
        res = ApiFactory.get_product_api().product_detail_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言包含关键字
        assert False not in [i in res.text for i in ['id', 'name', 'price', 'stock', 'main_img_url']]
        # 断言id属性值
        assert res.json().get('id') == 2
        # 断言 price
        assert res.json().get('price') == '0.01'
        # 断言name
        assert res.json().get('name') == '梨花带雨 3个'
