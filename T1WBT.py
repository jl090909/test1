import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import  datetime


class RT1():
	def test(self):
		runnumber=10
		#burl="http://www.businesstransforms.com"
		burl="https://ancient-chamber-55984.herokuapp.com/"
		driverLocation = "C:\\dj\\env1\\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = driverLocation
		driver = webdriver.Chrome(driverLocation)
		driver.maximize_window()
		driver.get(burl)
		driver.implicitly_wait(10)

		#test to_do_box
		test="test_add_to_do_list"
		xpth_tdl="//div[@id='navbarSupportedContent']//input[@name='item']"
		sbox=driver.find_elements(By.XPATH,xpth_tdl)
		for s in sbox:
			print (test + " if multiple xpath not unique")
			print( test + " State is_enabled " + " "+ str(s.is_enabled()))
			print( test + " State2 is_displayed "+ " "+ str(s.is_displayed()))
			ts=str(datetime.datetime.now())
			print(ts)
			s.send_keys( "RT" +str(runnumber) + "businesstransfors.com" + ts)
			xpth_adl_btn="//div[@id='navbarSupportedContent']//button[@class='btn btn-outline-secondary my-2 my-sm-0']"
			adl_btn=driver.find_element(By.XPATH,xpth_adl_btn)
			adl_btn.click()
		time.sleep(5)

		#test crypto 
		xpth_tdl="//div[@id='navbarSupportedContent']/ul[3]//a[@href='crypto/']"
		test="test_nav_bar_crypto_link"
		sbox=driver.find_elements(By.XPATH,xpth_tdl)
		for s in sbox:
			print (test + " if multiple xpath not unique")
			print( test + " State is_enabled " + " "+ str(s.is_enabled()))
			print( test + " State2 is_displayed "+ " "+ str(s.is_displayed()))
			ts=str(datetime.datetime.now())
			print(ts)
			#s.send_keys( "RT" +str(runnumber) + "businesstransfors.com" + ts)
			s.click()

		time.sleep(5)

		
e = RT1()
e.test()