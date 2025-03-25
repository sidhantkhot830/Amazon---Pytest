from selenium.webdriver.common.by import By


class LandingPage:

    def __init__(self,driver):
        self.driver = driver

    search_list = "//div[1]/a/h2/span"

    def verify_product(self,prod):

        ls = self.driver.find_elements(By.XPATH,self.search_list)
        for i in ls:
            if prod in i.text:
                assert True
                return
        assert False