from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base import BasePage
import time

class LeverCheck(BasePage):
    

    def check_lever(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains("lever.co"))
        print("Lever sayfasina gectim yani form acildi.")