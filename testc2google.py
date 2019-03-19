import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class CT1():
	def test(self):
		burl="http://WWW.GOOGLE.COM"
		driverLocation = "C:\\dj\\env1\\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = driverLocation
		driver = webdriver.Chrome(driverLocation)
		driver.maximize_window()
		driver.get(burl)
		driver.implicitly_wait(10)
		sbox=driver.find_elements(By.XPATH,"/html//form[@id='tsf']//div[@class='a4bIc']/input[@role='combobox']")
		for s in sbox:
			print( "State "+ str(s.is_enabled()))
			print( "State2 "+ str(s.is_displayed()))

		
				
		#loginlink.click()
		#print( "State "+ str(sbox.is_enabled()))

			s.send_keys("businesstransfors.com")

		
e = CT1()
e.test()