from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base import BasePage
import time

class lever_check(BasePage):
    location_filter = (By.XPATH, "//div[@aria-label='Filter by Location: All']")
    team_filter = (By.XPATH, "//div[@aria-label='Filter by Team: Software Development']")
#filtre uygulama
    def apply_filters(self):
        self.js_click(self.location_filter)
        time.sleep(2)
        self.scroll_to_element((By.XPATH, "//a[@class='category-link' and text()='Istanbul, Turkiye']"))
        time.sleep(2)
        self.js_click((By.XPATH, "//a[@class='category-link' and text()='Istanbul, Turkiye']"))
        time.sleep(2)
        print("konum için tiklayabildim.")
        self.js_click(self.team_filter)
        time.sleep(2)
        self.scroll_to_element((By.XPATH, "//a[@class='category-link' and text()='Quality Assurance']"))
        time.sleep(2)
        self.js_click((By.XPATH, "//a[@class='category-link' and text()='Quality Assurance']"))
        time.sleep(2)
        self.check_filters()

    def check_filters(self):

        postings = self.driver.find_elements(By.CSS_SELECTOR, ".posting") #listee
        
        if not postings:
            raise Exception(" hic is ilani bulunamadi")
#ilanların konumunu ve içerigini kontrol etme
        invalid_jobs = [] 

        for job in postings:
            job_text = job.text.lower()
            
            is_valid = "istanbul, turkiye" in job_text and "quality" in job_text
            
            if not is_valid:
                
                invalid_jobs.append(job.text.split('\n')[0])
        
        if invalid_jobs:
            raise Exception(f"filtreleme kriterlerine uymayan is ilanlari: {invalid_jobs}")

        

    def click_qajob(self):
        self.js_click((By.XPATH, "//a[contains(@class, 'posting-btn-submit') and text()='Apply']"))
        time.sleep(2)
        print("QA jobuna tiklayabildim.")