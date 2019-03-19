import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class CT1():
	def test(self):
		burl="http://www.businesstransforms.com"
		driverLocation = "C:\\dj\\env1\\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = driverLocation
		driver = webdriver.Chrome(driverLocation)
		driver.maximize_window()
		driver.get(burl)
		driver.implicitly_wait(10)
		loginlink=driver.find_element(By.XPATH,"//a[contains(text(),'Authenticate')]")
		loginlink.click()
		time.sleep(3)
		loginlink=driver.find_element(By.XPATH,"//div[@id='navbarSupportedContent']/ul[1]//a[@href='/accounts/login/']")
		loginlink.click()
		time.sleep(5)
		

chromeTest = CT1()
chromeTest.test()