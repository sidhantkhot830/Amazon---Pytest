import pytest

from pages.homepage import HomePage
from pages.landingpage import LandingPage


@pytest.mark.usefixtures("setup")
class Test_search:

    def setup_method(self):
        self.driver.get("https://www.amazon.in/")
        self.hp = HomePage(self.driver)
        self.lp = LandingPage(self.driver)



    def test_search_existing(self):
        self.hp.enter_search("HP pavilion")
        self.hp.click_search()
        self.lp.verify_product("HP Pavilion")