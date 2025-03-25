from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_box = "//input[@id='twotabsearchtextbox']"
    search_button ="//input[@id='nav-search-submit-button']"
    def enter_search(self,prod_name):
        self.driver.find_element(By.XPATH,self.search_box).send_keys(prod_name)

    def click_search(self):
        self.driver.find_element(By.XPATH,self.search_button).click()