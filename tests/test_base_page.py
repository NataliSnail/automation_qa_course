import time
from pages.base_page import BasePage
def test_open_page(driver):
    page = BasePage(driver,'https://demoqa.com/elements')
    page.open()
    time.sleep(3)