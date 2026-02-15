from selenium.webdriver.common.by import By
from .base import BasePage
import time

class CareerPage(BasePage):
    
    career_link = (By.XPATH, "//div[contains(@class, 'insiderone-hero-banner-content-buttons')]//a")
    software_development_link = (By.XPATH, "//a[contains(@href, 'Software%20Development')]")
    def click_explore(self):
        self.js_click(self.career_link)
        time.sleep(2)
        print("is butonuna tikladim bea.")
        self.scroll_to_element(self.software_development_link)
        self.js_click(self.software_development_link)
        print("software development kartina tikladim.")