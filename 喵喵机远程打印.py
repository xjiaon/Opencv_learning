import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://t.cn/R9U4xwG")
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("editor")
        elem.send_keys("印度儿童纪录片")
        #time.sleep(5)
        #elem.clear()
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source
        ele=driver.find_element_by_tag_name("input")
        #<i class="icon-pic iconfont icon-mailbox_icon_addpic_1"></i>
        time.sleep(2)
        #ele.click()
        print ("done")
        ele.send_keys("c:\\temp\\1.jpg")
        time.sleep(5)
        driver.find_element_by_id("btnPreview").click()
 
    def tearDown(self):
        #self.driver.close()
        pass
 
if __name__ == "__main__":
    unittest.main()
