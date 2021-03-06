import pytest
from selenium import webdriver
from pageObjects.loginpage import loginpage
from utilities.readproperties import Readconfig
from utilities.customlogger import logGen
from utilities import XLutil
import time

class Test_002_login:

    baseURL=Readconfig.getapplicaionurl()
    path=".\\testdata\\data.xlsx"
    logger=logGen.loggen()

    def test_homepage_DDT(self,setup):
        self.logger.info("****** Test_002_Login_DDT******")
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

    def test_loginpage_DDT(self,setup):
        self.logger.info ( "****** Test_002_Login_DTT ******" )
        self.logger.info ( "****** Verifying Login page Title ********" )
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=loginpage(self.driver)
        self.rows=XLutil.getRowcount(self.path,'Sheet1')
        print("Number of rows in sheet:",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLutil.readData(self.path,'Sheet1',r,1)
            self.password=XLutil.readData(self.path,'Sheet1',r,2)
            self.exp=XLutil.readData(self.path,'Sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp =='Pass':
                    self.logger.info("******* Title matched and Passed ********")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp =='Fail':
                    self.logger.info ( "******* Title not matched and Failed ********" )
                    self.lp.clicklogout ()
                    lst_status.append ( "Fail" )

            elif act_title != exp_title:

                if self.exp == "Pass":
                    self.logger.info("******* Failed *******")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info ( "******* Passed *******" )
                    lst_status.append ("Pass")

                if "Fail" not in lst_status:
                    self.logger.info("Login DDT Test Passed")
                    self.driver.close()
                    assert True
            else:
                self.logger.info("Login DDT Test Failed")
                self.driver.close()
                assert False
        self.logger.info("****** End of the Login DDT ***********")
        self.logger.info("****** Completed TC_Login_002_DDT ******")

