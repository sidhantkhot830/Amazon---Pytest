import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request,browser):
    driver = None
    if "chrome"==browser:
        option = webdriver.ChromeOptions()
        service = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service ,options=option)
    if "ff"==browser:
        option = webdriver.FirefoxOptions()
        service = webdriver.FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service,options=option)
    if "edge"==browser:
        option = webdriver.EdgeOptions()
        service = webdriver.EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service,options=option)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")