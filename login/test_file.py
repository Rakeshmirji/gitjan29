import time

import pytest
from selenium.webdriver.common.by import By
from login.home_page import HomePage

#for loggin import
@pytest.mark.usefixtures("setup")
class Test_001:
    def test_001(self):
        hell=HomePage(self.driver)
        hell.test_login()
        hell.test_create_account()