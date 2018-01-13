import unittest

from frame_base_class.driver_base import Drivrser_base  # 浏览器驱动
from test_case.Login_and_register.Test_login import Skin01_login
from test_case.Order_processing.Test_new_order import new_order


class MyTestCase(unittest.TestCase):

    login = Skin01_login()
    new_or = new_order()

    @classmethod
    def setUpClass(self):
        browser = Drivrser_base(self)
        self.browser = browser.open_browser(self)
        # self.browser = browser.open_browser()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()


    def test_login_case(self):
        browser = self.browser
        self.login.user_login(browser)


    def test_new_order(self):
        browser = self.browser
        self.new_or.new_order_manual_input(browser)

if __name__ == '__main__':
    unittest.main()



