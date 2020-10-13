import pytest

from Api.apiFactory import ApiFactory
import app
import utils, logging


@pytest.mark.run(order=0)
class TestUserApi:
    """用户权限测试类"""

    def test_token_user_api(self):
        res = ApiFactory.get_user_api().token_user_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言响应状态码
        # assert res.status_code == 200
        utils.common_assert_code(res, 200)
        # 断言包含token存在
        assert len(res.json().get('token')) > 0
        # 保存token
        app.headers['token'] = res.json().get('token')

    def test_token_verify_api(self):
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res, 200)
        # 断言值为true
        assert res.json().get('isValid') is True

    def test_address_api(self):
        res = ApiFactory.get_user_api().address_api()
        # 打印请求地址，打印请求参数 打印响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据：{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res, 200)
        # 大于0
        assert len(res.json()) > 0
        # 包含关键字
        # assert res.json().get('name') == '肖肖' and res.json().get('city') == '上海市' \
        #        and res.json().get('country') == '浦东区' \
        #        and res.json().get('mobile') == '13862812345'
        # 断言信息
        assert False not in [i in res.text for i in ['肖肖', '13862812345', '浦东区', '上海市']]
