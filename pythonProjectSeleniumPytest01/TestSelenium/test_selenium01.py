import unittest
from selenium import webdriver
class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    # Je lance tous les tests contenus dans ce fichier.
    unittest.main(verbosity=2)

