from Api.apiFactory import ApiFactory

# print(ApiFactory.get_home_api().banner_api().json())
#
# print(ApiFactory.get_home_api().theme_api().json())
#
# print(ApiFactory.get_home_api().product_recent_api().json())


# print(ApiFactory.get_product_api().product_classify_api().json())
# print(ApiFactory.get_product_api().classify_product_api(5).json())
# print(ApiFactory.get_product_api().product_detail_api(26).json())

# print(ApiFactory.get_user_api().token_user_api().json())

print(ApiFactory.get_order_api().order_list_api().json())
print(ApiFactory.get_order_api().create_order_api(12, 1).json())
print(ApiFactory.get_order_api().query_order_pai(99).json())
