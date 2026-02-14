from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base import BasePage
import time

class lever_check(BasePage):
    location_filter = (By.XPATH, "//div[@aria-label='Filter by Location: All']")
    team_filter = (By.XPATH, "//div[@aria-label='Filter by Team: Software Development']")

    def apply_filters(self):
        self.js_click(self.location_filter)
        time.sleep(2)
        self.scroll_to_element((By.XPATH, "//a[@class='category-link' and text()='Istanbul, Turkiye']"))
        time.sleep(2)
        self.js_click((By.XPATH, "//a[@class='category-link' and text()='Istanbul, Turkiye']"))
        time.sleep(2)
        print("konum için tıklayabildim mi bea.")
        self.js_click(self.team_filter)
        time.sleep(2)
        self.scroll_to_element((By.XPATH, "//a[@class='category-link' and text()='Quality Assurance']"))
        time.sleep(2)
        self.js_click((By.XPATH, "//a[@class='category-link' and text()='Quality Assurance']"))
        time.sleep(2)

    def click_qajob(self):
        self.js_click((By.XPATH, "//a[contains(@class, 'posting-btn-submit') and text()='Apply']"))
        time.sleep(2)
        print("QA jobuna tiklayabildim mi bea.")