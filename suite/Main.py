#coding=utf-8      #��ֹ��������

import unittest 
import HTMLTestRunner
from case import test1


if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(test1.test1("test_ems"))

    fp=open("����"+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'����:')
    runner.run(testunit) 
    fp.close()