import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
class Exercice1(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        self.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.browser.find_element(By.NAME, 'username').clear()
        self.browser.find_element(By.NAME, 'username').send_keys('Admin')
        self.browser.find_element(By.NAME, 'password').clear()
        self.browser.find_element(By.NAME, 'password').send_keys('admin123')
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_logout(self):
        self.test_login()
        self.browser.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        self.browser.find_element(By.LINK_TEXT, 'Logout').click()

    def test_loginKO(self):
        self.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.browser.find_element(By.NAME, 'username').clear()
        self.browser.find_element(By.NAME, 'username').send_keys('Jean-Luc Melanchon')
        self.browser.find_element(By.NAME, 'password').clear()
        self.browser.find_element(By.NAME, 'password').send_keys('Meluche')
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    # Je lance tous les tests contenus dans ce fichier.
    unittest.main()