import pytest

from pages.googlepage import GooglePage


@pytest.mark.usefixtures("setup")
class Test_Demo:

    def setup_method(self):
        self.Gp = GooglePage(self.driver)

    def test_001_demo(self):
        self.Gp.driver.get("http://google.com")
        title = self.Gp.driver.title
        assert "Google" == title
