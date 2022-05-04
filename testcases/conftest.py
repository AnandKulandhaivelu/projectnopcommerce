from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver=webdriver.Chrome(executable_path="C:\DRIVERS\Chrome\chromedriver.exe")
        print("Lanching Chrome browser......")

    else:
        driver = webdriver.Chrome ( executable_path="C:\DRIVERS\Chrome\chromedriver.exe" )
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['project name']='Nop commerce'
    config._metadata['Module name']='Customers'
    config._metadata['Tester']='Anand'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_home",None)
    metadata.pop("plugins",None)


