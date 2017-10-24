from selenium import webdriver

browser=webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.facebook.com')

browser.find_element_by_xpath("//input[@id='email']").send_keys("9970470663")
browser.find_element_by_xpath("//input[@id='pass']").send_keys("kirti123#")
browser.find_element_by_xpath("//input[@type='submit']").click()
browser.quit()
