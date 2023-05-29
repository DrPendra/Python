from test_Exercice1 import Exercice1
from selenium.webdriver.common.by import By

import pytest

@pytest.fixture
def ex():
    return Exercice1

def test_ordre_changer(ex):
    ex=ex()
    ex.setUp()
    ex.test_logout()
    ex.test_loginKO()
    ex.test_login()

def test_ajouter(ex):
    ex=ex()
    ex.setUp()
    ex.browser.get('https://www.google.fr/')
    ex.test_login()

def test_modifier(ex):
    user='oui'
    pw='non'
    ex = ex()
    ex.setUp()
    ex.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    ex.browser.find_element(By.NAME, 'username').clear()
    ex.browser.find_element(By.NAME, 'username').send_keys(str(user))
    ex.browser.find_element(By.NAME, 'password').clear()
    ex.browser.find_element(By.NAME, 'password').send_keys(str(pw))
    ex.browser.find_element(By.XPATH, "//button[@type='submit']").click()

def test_connection(ex):
    ex = ex()
    ex.setUp()
    ex.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    ex.browser.implicitly_wait(10)
    ex.test_login()

def test_deconexion(ex):
    ex = ex()
    ex.setUp()
    ex.test_logout()






