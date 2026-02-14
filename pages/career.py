from selenium.webdriver.common.by import By
from .base import BasePage
import time

class CareerPage(BasePage):
    
    career_link = (By.XPATH, "//div[contains(@class, 'insiderone-hero-banner-content-buttons')]//a")
    software_development_link = (By.XPATH, "//a[contains(@href, '/careers/job/software-developer/')]")
    def click_explore(self):
        self.js_click(self.career_link)
        time.sleep(2)
        print("is butonuna tikladim bea.")