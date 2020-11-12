from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class Base():
    '''
    #��ʼ��
    '''
    def __init__(self, driver):
        self.driver = driver
    
    '''
    #����ҳ��Ԫ��
    '''
    def getWebElement(self,webElement):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(eval(webElement)))
        we='self.driver.find_element('+str(webElement)+')'
        return eval(we)
    
    '''
    #����
    '''
    def inputValue(self,webElement,value):
        self.clear(webElement)
        self.getWebElement(webElement).send_keys(value)
        
    '''
    #ѡ�������б�
    '''
    def selValue(self,webElement,value):
        sel=self.getWebElement(webElement)
        Select(sel).select_by_value(value)
        
    '''
    #���
    '''
    def click(self,webElement):
        self.getWebElement(webElement).click()
        
    '''
    #��ȡԪ��ֵ
    '''
    def getValue(self,webElement):
        return self.getWebElement(webElement).text
        
    '''
    #��ȡԪ������ֵ
    '''
    def getAttValue(self,webElement,att):
        return self.getWebElement(webElement).get_attribute(att)
    
    '''
    #���
    '''
    def clear(self,webElement):
        self.getWebElement(webElement).clear()
        
    '''
    #ѡ��frame
    '''
    def selFrame(self, webElement):
        return self.driver.switch_to_frame(webElement)
    
    '''
    #����script����������ִ��js�ű�����Χִ�н��
    '''
    def script(self, src):
        self.driver.execute_script(src)
        
    '''
         ��ȡ�����б�ѡ��ֵ
     @param webElement    ҳ��Ԫ��
    '''
    def getSeclected(self, webElement):
        self.waitForLoad(webElement)
        return self.getWebElement(webElement).get_attribute('value')
        
    '''
           ��ȡ�����б�����
     @param webElement    ҳ��Ԫ��
     @return
    '''
    def getArraly(self, webElement):
        self.waitForLoad(webElement)
        return self.getWebElement(webElement).text
        
    '''
    #�ȴ�Ԫ�ؼ������ 10s
    '''
    def waitForLoad(self,webElement):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(eval(webElement)))
        
    '''
          �ȴ�ĳԪ����ʧ
     @param locator   ��λ��
     @param timeOut   ��ʱʱ��
    '''
    def waitForDisapp(self):
        pass

    '''
     * ��λ���´򿪵Ĵ���
    '''
    def selNewWindow(self):
        pass
        
    '''
          ҳ�����
     @param offset  0     �Ƕ��� 
                     10000 �ǵײ�
    '''
   # def scroll(self, offset):
    #    JavascriptExecutor driver_js= (JavascriptExecutor) driver
    #    driver_js.executeScript("window.scrollTo(0,"+offset+")")
    
    '''
    #��ȡԪ������
    '''
    def getLocation(self,webElement):
        loca = self.findElement(webElement).location
        return str(loca).replace('{', '(').replace('}', ')').replace("'x': ", "").replace(" 'y': ", "")
    
    '''
      x����
    '''
    def getX(self, webElement):
        self.waitForLoad(webElement);
        location = self.getLocation(webElement)
        return location[1:str(location).find(',')]
    
    '''
     * Y����
    '''
    def getY(self, webElement):
        self.waitForLoad(webElement);
        location = self.getLocation(webElement)
        return location[str(location).find(',')+1:len(str(location))-1]
    
        
    '''
            У�����־���
      @param webElement   ҳ��Ԫ��
      @return   С������λ��
    '''
    def getAccuracy(self, webElement):
        self.waitForLoad(webElement);
        value =self.getValue(webElement)
        long = len(value[value.find('.')+1:len(value)])
        return long      
        
    '''
            У�����־���
      @param value  ��ҪУ����ַ���
      @return   С������λ��
    '''
    def getStrAccuracy(self,value):
        long = len(value[value.find('.')+1:len(value)])
        return long       
    
    '''
    #�ر������
    '''
    def close(self):
        self.driver.close()