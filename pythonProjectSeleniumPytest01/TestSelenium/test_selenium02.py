import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

'''
https://selenium-python.readthedocs.io/index.html
https://docs.python.org/fr/3/library/pydoc.html
'''
class AvosclicsTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://a-vos-clics-formation.fr/')
        self.assertIn('@ Vos Clics', self.browser.title)

    def test_page_contenu(self):
        self.browser.get('http://a-vos-clics-formation.fr/')
        contenu = self.browser.find_elements(By.ID, 'header')
        self.assertIsInstance(contenu, list)
        self.assertEqual(len(contenu), 1)
        for c in contenu:
            # Je recherche explicitement une seule balise dont l'id = 'logo'
            # par l'utilisation de la méthode find_element(...)
            t = c.find_element(By.ID, 'logo')
            self.assertIsInstance(t, WebElement)
            # Je dois avoir une instance de type WebElement (balise HTML)

if __name__ == '__main__':
    unittest.main(verbosity=2)