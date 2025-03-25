import pytest
from pages.googlepage import GooglePage

# @pytest.mark.usefixtures("setup",)
class Test_Demo:

    def setup_method(self):
        # self.driver.get("https://www.amazon.in/")
        self.Gp = GooglePage(self.driver)


    def test_001_demo(self,logger):
        logger.info("test_001_demo".upper())
        self.Gp.driver.get("http://google.com")
        title = self.Gp.driver.title
        logger.info("checking for Google in page title")
        assert "Google" == title, "Google not found in page title"
        logger.info("Google found in page title ")

    def test_002_search_existing_prod(self,logger):
        logger.info("test_002_search_existing_prod".upper())
        txt = "HP Pavilion x360, 13th Gen Intel Core i5-1335U,16GB DDR4, 512GB SSD, (Win11,Office 21, Silver,1.51kg), Touchscreen, 14-inch(35.6cm), FHD Laptop, Iris Xe, FPR, 5MP Camera, Backlit KB, Pen, ek1074TU"
        logger.info("searching for HP pavilion in product list")
        assert "HP pavilion".lower() in txt.lower() , "HP pavilion not found in txt"
        logger.info("HP pavilion found in list")

