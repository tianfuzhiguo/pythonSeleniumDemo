from selenium import webdriver
from Base.Base import Base
from selenium.webdriver.common.by import By
from Base.Variable import *

'''
Created on 2018年1月12日

@author: dujianxiao
'''

class Util(Base):
    
    @staticmethod
    def login(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.driver.get(frontUrl)
        self.driver.maximize_window() 
        self.driver.find_element(By.NAME,'username').send_keys(frontUsername)
        self.driver.find_element(By.NAME,'password').send_keys(frontPassword)
        self.driver.find_element(By.CLASS_NAME,'btnLogin').click()
        try:
            self.click("By.CSS_SELECTOR,'button.confirm.btn.btn-blue-small'")
        except Exception:
            pass
        self.waitForLoad("By.LINK_TEXT,'能源管理'")

    def chooseMenu(self,first, second):
        self.click("By.LINK_TEXT,'"+first+"'")
        self.click("By.CSS_SELECTOR,'b.navbar_hide'")
        self.waitForLoad("By.LINK_TEXT,'"+second+"'")
        self.click("By.LINK_TEXT,'"+second+"'")   