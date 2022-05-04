import pytest
from selenium import webdriver
from pageObjects.loginpage import loginpage
from utilities.readproperties import Readconfig
from utilities.customlogger import logGen

class Test_001_login:

    baseURL=Readconfig.getapplicaionurl()
    username=Readconfig.getusermail()
    password=Readconfig.getpasswod()

    logger=logGen.loggen()

    def test_homepage(self,setup):
        self.logger.info("****** Test_001_Login******")
        self.logger.info("****** Verifying Home page Title ********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            self.logger.info("******* Homepage title test is passed ********")
            assert True

        else:
            self.driver.save_screenshot(".//screenshots//" + "Home_page.png")
            self.logger.info ( "******* Homepage title test is Failed ********" )
            self.driver.close()
            assert False

    def test_loginpage(self,setup):
        self.logger.info ( "****** Test_001_Login ******" )
        self.logger.info ( "****** Verifying Login page Title ********" )
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info ( "******* Login page title test is passed ********" )
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "Test_loginpage.png")
            self.logger.info ( "******* login page title test is failed ********" )
            self.driver.close ()
            assert False

