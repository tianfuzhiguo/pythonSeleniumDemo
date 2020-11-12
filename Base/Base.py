from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class Base():
    '''
    #初始化
    '''
    def __init__(self, driver):
        self.driver = driver
    
    '''
    #查找页面元素
    '''
    def getWebElement(self,webElement):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(eval(webElement)))
        we='self.driver.find_element('+str(webElement)+')'
        return eval(we)
    
    '''
    #输入
    '''
    def inputValue(self,webElement,value):
        self.clear(webElement)
        self.getWebElement(webElement).send_keys(value)
        
    '''
    #选择下拉列表
    '''
    def selValue(self,webElement,value):
        sel=self.getWebElement(webElement)
        Select(sel).select_by_value(value)
        
    '''
    #点击
    '''
    def click(self,webElement):
        self.getWebElement(webElement).click()
        
    '''
    #获取元素值
    '''
    def getValue(self,webElement):
        return self.getWebElement(webElement).text
        
    '''
    #获取元素属性值
    '''
    def getAttValue(self,webElement,att):
        return self.getWebElement(webElement).get_attribute(att)
    
    '''
    #清空
    '''
    def clear(self,webElement):
        self.getWebElement(webElement).clear()
        
    '''
    #选择frame
    '''
    def selFrame(self, webElement):
        return self.driver.switch_to_frame(webElement)
    
    '''
    #定义script方法，用于执行js脚本，范围执行结果
    '''
    def script(self, src):
        self.driver.execute_script(src)
        
    '''
         获取下拉列表选中值
     @param webElement    页面元素
    '''
    def getSeclected(self, webElement):
        self.waitForLoad(webElement)
        return self.getWebElement(webElement).get_attribute('value')
        
    '''
           获取下拉列表数组
     @param webElement    页面元素
     @return
    '''
    def getArraly(self, webElement):
        self.waitForLoad(webElement)
        return self.getWebElement(webElement).text
        
    '''
    #等待元素加载完成 10s
    '''
    def waitForLoad(self,webElement):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(eval(webElement)))
        
    '''
          等待某元素消失
     @param locator   定位器
     @param timeOut   超时时间
    '''
    def waitForDisapp(self):
        pass

    '''
     * 定位到新打开的窗口
    '''
    def selNewWindow(self):
        pass
        
    '''
          页面滚动
     @param offset  0     是顶部 
                     10000 是底部
    '''
   # def scroll(self, offset):
    #    JavascriptExecutor driver_js= (JavascriptExecutor) driver
    #    driver_js.executeScript("window.scrollTo(0,"+offset+")")
    
    '''
    #获取元素坐标
    '''
    def getLocation(self,webElement):
        loca = self.findElement(webElement).location
        return str(loca).replace('{', '(').replace('}', ')').replace("'x': ", "").replace(" 'y': ", "")
    
    '''
      x坐标
    '''
    def getX(self, webElement):
        self.waitForLoad(webElement);
        location = self.getLocation(webElement)
        return location[1:str(location).find(',')]
    
    '''
     * Y坐标
    '''
    def getY(self, webElement):
        self.waitForLoad(webElement);
        location = self.getLocation(webElement)
        return location[str(location).find(',')+1:len(str(location))-1]
    
        
    '''
            校验数字精度
      @param webElement   页面元素
      @return   小数点后的位数
    '''
    def getAccuracy(self, webElement):
        self.waitForLoad(webElement);
        value =self.getValue(webElement)
        long = len(value[value.find('.')+1:len(value)])
        return long      
        
    '''
            校验数字精度
      @param value  需要校验的字符串
      @return   小数点后的位数
    '''
    def getStrAccuracy(self,value):
        long = len(value[value.find('.')+1:len(value)])
        return long       
    
    '''
    #关闭浏览器
    '''
    def close(self):
        self.driver.close()