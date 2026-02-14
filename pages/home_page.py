from selenium.webdriver.common.by import By
from .base import BasePage

class HomePage(BasePage):
    
    hiring_link = (By.XPATH, "//div[contains(@class, 'footer')]//a[@href='/careers/']")

    def go_to_url(self):
        self.driver.get("https://useinsider.com/")
        self.scroll_to_element(self.hiring_link)
        self.js_click(self.hiring_link)
        print("butona tikladim bea.")
        
        