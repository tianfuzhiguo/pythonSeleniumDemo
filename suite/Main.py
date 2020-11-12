#coding=utf-8      #·ÀÖ¹ÖĞÎÄÂÒÂë

import unittest 
import HTMLTestRunner
from case import test1


if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(test1.test1("test_ems"))

    fp=open("²âÊÔ"+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'²âÊÔ:')
    runner.run(testunit) 
    fp.close()