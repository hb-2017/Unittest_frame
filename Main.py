import unittest
from frame_base_class.driver_base import  Drivrser_base #浏览器驱动
from test_case.login_case import Skin01_login


class MyTestCase(unittest.TestCase):

    login = Skin01_login()

    def setUp(self):
        browser = Drivrser_base(self)
        self.browser = browser.open_browser(self)

    def tearDown(self):
        self.browser.quit()


    def test_login_case(self):
        browser = self.browser
        self.login.user_login(browser)





if __name__ == '__main__':
    unittest.main()
