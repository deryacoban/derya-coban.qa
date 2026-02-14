import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    # 15sn bekleme
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
    #  scrolll into view
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

#    def select_from_dropdown(self, option_text):

#            target_option = self.driver.find_element(By.XPATH, f"//*[text()='{option_text}']")
#            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_option)
#            target_option.click()
        
        
        
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
#tıkllama
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
#tıklama js
    def js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)
#ekran görüntüsü
    def take_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")
    # wait
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    # locator bekleme 
    def wait_and_click(self, locator):
        element = self.wait_for_element_clickable(locator)
        if element:
            element.click()
        else:
            #ss alma
            raise Exception(f"Elemente tiklanamadi: {locator}")