import pytest
from selenium import webdriver
from PageObejcts.LoginPage import Loginpage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test__001_Login:

    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setuseremail(self.useremail)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        self.logger.info("**** Login test passed ****")