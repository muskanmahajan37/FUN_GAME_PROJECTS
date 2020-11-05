from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#web driver  location : "C:\\Users\\ag16000\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe"
#driver.set_page_timeout("10")
data = input("enter something you want to search: ")
driver.implicitly_wait(5)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys(data)
driver.implicitly_wait(5)
#try
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
#or
button = driver.find_element_by_class_name("gNO89b")
button.click()
driver.maximize_window()
driver.refresh()

time.sleep(4)
driver.quit()