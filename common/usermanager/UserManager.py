from common.usermanager.UserManagerWebElement import UserManagerWebElement
from utils.Util import Util
import time
'''
 #用户管理页面
 @author dujianxiao
'''

class UserManager(UserManagerWebElement):

    '''
    #初始化
    '''
    def init(self):
        Util.login(self)
        Util.chooseMenu(self, '平台管理', '用户管理')

    '''
     # 查询结果某行某列的值
     @param param:   row      行号
     @param column   1序号、2登录账户、3用户姓名、4所属部门、5是否主管、6是否外包、7所属角色、8状态、9手机号
     @return
     '''
    def getRes(self, row, column):
        time.sleep(2)
        webElement="By.XPATH,"+'''"//*[@id='content']/div/div/div/div[2]/div[2]/table/tbody/tr[''' + str(row) + "]/td[" + str(column) + ''']"'''
        self.waitForLoad(webElement)
        return self.getValue(webElement);
    s