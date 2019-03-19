from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class CT1():
	def test(self):
    	driverLocation = "C:\\dj\\env1\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.businesstransforms.com")
     	EById=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "navbarSupportedContent"))  )
    	driver.quit()

chromeTest = CT1()
chromeTest.test()