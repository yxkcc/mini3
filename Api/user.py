import logging

import requests
import app


class UserApi:
    def __init__(self):
        # 获取token
        self.token_user_url = app.base_url + "/token/user"
        # token验证
        self.token_verify_url = app.base_url + "/token/verify"
        # 获取地址信息
        self.address_url = app.base_url + "/address"

    def token_user_api(self):
        """获取token"""
        logging.info("获取token")
        data = {'code': app.code}
        logging.info('请求参数：{}'.format(data))
        return requests.post(self.token_user_url, headers=app.headers, json=data)

    def token_verify_api(self):
        """验证token"""
        logging.info("验证token")
        data = {'token': app.headers.get('token')}
        logging.info('请求参数：{}'.format(data))
        return requests.post(self.token_verify_url, headers=app.headers, json=data)

    def address_api(self):
        """获取地址"""
        logging.info("获取地址")
        return requests.get(self.address_url, headers=app.headers)
