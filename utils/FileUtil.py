import configparser
import os
from utils.Variable import *

'''
Created on 2018��1��11��
@author: dujianxiao
'''

class FileUtil():
   
    '''
   ��#��ȡ�����ļ�
    '''
    @staticmethod
    def getValue(fileName,key):
        config = configparser.ConfigParser()
        config.readfp(open(fileName))
        value = config.get('section',key)
        return value
    
    '''
    ��#ɾ���ļ�
    '''
    @staticmethod
    def deleteFile(fileName):
        try:
            os.remove(filePath1+fileName)
        except Exception:
            pass
        
    '''
    ��#У���ļ��Ƿ����
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