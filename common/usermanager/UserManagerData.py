from Base.Base import Base

'''
#用户管理页面数据
@author: dujianxiao
'''
class UserManagerData(Base):
    '''
    #是否主管
    '''
    manager = "1"
    notManager = "0"

    '''
    #是否外包
    '''
    out = "1"
    notOut = "0"

    '''
    #状态
    '''
    enable = "1"
    disable = "0"

    '''
    #查询条件
    '''
    dept = "公司总部";