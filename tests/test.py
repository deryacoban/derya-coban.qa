from tabnanny import check
import unittest
import sys
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.career import CareerPage
from pages.home_page import HomePage
from pages.base import BasePage
from pages.lever import lever_check
from pages.lever_check import LeverCheck

class InsiderCareerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10000)
        self.home_page = HomePage(self.driver)
        self.career = CareerPage(self.driver)
        self.base_page = BasePage(self.driver)
        self.lever = lever_check(self.driver)
        self.lever_check = LeverCheck(self.driver)
        
        

    def test_job_application_flow(self):
        try:
            self.home_page.go_to_url()
            
            self.career.click_explore()

            self.lever.apply_filters()
            self.lever.check_filters()
            self.lever.click_qajob()


            self.lever_check.check_lever()

            
            
        except Exception as e:
            self.home_page.take_screenshot("hata_anlik_goruntu")
            print(f" test basarisiz ekran goruntusunu kontrol edin Hata: {e}")
            raise e 
        """def test_career(self):
            try:
                self.career.click_explore()
            except Exception as e:
                self.home_page.take_screenshot("hata_anlik_goruntu")
                print(f" is ilanlari acilmadi: {e}")
                raise e """

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()