import unittest 
from common.usermanager.UserManager import UserManager

'''
#用户管理－－用户查询
@author dujianxiao
'''

class test1(unittest.TestCase,UserManager):
    def setUp(self):
        self.init()
       
    def test_ems(self):
        self.selValue(self.isManager, self.manager)
        self.selValue(self.isOut, self.notOut)
        self.selValue(self.status, self.enable)
        self.inputValue(self.keyword, self.dept)
        self.click(self.queryBtn)
        self.assertTrue(self.getRes(1, 4)==self.dept)
       
    def tearDown(self):
        self.close()
 

if __name__ == "__main__":
    unittest.main()
   
