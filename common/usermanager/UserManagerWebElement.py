from common.usermanager.UserManagerData import UserManagerData

'''
#用户管理页面元素
@author dujianxiao
'''
class UserManagerWebElement(UserManagerData):
    isManager = "By.CSS_SELECTOR,'select.select_manage.mb10.select2.select2-offscreen'"
    isOut= "By.CSS_SELECTOR,'select.select_out.ml10.select2.select2-offscreen'"
    status = "By.CSS_SELECTOR,'select.select_status.ml10.select2.select2-offscreen'"
    keyword = "By.CSS_SELECTOR,'input.role_keyword.role_query_input'"
    queryBtn= "By.ID,'addRole'"