from selenium import webdriver
import os

class RunChromeTestsWindows():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        driverLocation = "C:\\djangostuff\\env2\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.businesstransforms.com")

chromeTest = RunChromeTestsWindows()
chromeTest.test()