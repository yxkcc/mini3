def common_assert_code(res, code):
    """
    通用断言
    :param res:
    :param code:
    :return:
    """
    assert res.status_code == code
