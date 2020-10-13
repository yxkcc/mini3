import utils
from Api.apiFactory import ApiFactory
import logging


class TestHomeApi:
    """主页接口测试类"""

    def test_banner_api(self):
        """轮播图"""
        # 请求返回数据
        res = ApiFactory.get_home_api().banner_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言id和name
        assert res.json().get('id') == 1 and res.json().get('name') == '首页置顶'
        # 断言items列表长度大于0
        assert len(res.json().get('items')) > 0

    def test_theme_api(self):
        """专题栏"""
        res = ApiFactory.get_home_api().theme_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言 三个id=1,2,3
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言 关键字段 name description topic_img head_img
        # ls = ['name', 'description', 'topic_img', 'head_img']
        # for i in ls:
        #     assert i in res.text
        assert False not in [i in res.text for i in ['name', 'description', 'topic_img', 'head_img']]

    def test_product_recent_api(self):
        """最近新品"""
        res = ApiFactory.get_home_api().product_recent_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res, 200)
        # 断言新品数量大于0
        assert len(res.json()) > 0
        # 断言关键字段
        assert False not in [i in res.text for i in ['id', 'name', 'price']]
