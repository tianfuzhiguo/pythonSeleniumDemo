import configparser
import os
from utils.Variable import *

'''
Created on 2018年1月11日
@author: dujianxiao
'''

class FileUtil():
   
    '''
   　#读取配置文件
    '''
    @staticmethod
    def getValue(fileName,key):
        config = configparser.ConfigParser()
        config.readfp(open(fileName))
        value = config.get('section',key)
        return value
    
    '''
    　#删除文件
    '''
    @staticmethod
    def deleteFile(fileName):
        try:
            os.remove(filePath1+fileName)
        except Exception:
            pass
        
    '''
    　#校验文件是否存在
    '''
    @staticmethod
    def isFileExist(fileName):
        flag = os.path.exists(filePath1+fileName)
        return flag
    
    @staticmethod
    def getCellValue(fileName):
        pass
    
    @staticmethod
    def setDate(time):
        os.system("date -s "+time)