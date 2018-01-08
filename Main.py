import unittest
from frame_base_class.driver_base import  Drivrser_base #浏览器驱动
from test_case.login_case import Skin01_login
from test_case.new_order_case import new_order


class MyTestCase(unittest.TestCase):

    login = Skin01_login()
    new_or = new_order()

    def setUp(self):
        browser = Drivrser_base(self)
        self.browser = browser.open_browser(self)

    def tearDown(self):
        self.browser.quit()


    def test_login_case(self):
        browser = self.browser
        self.login.user_login(browser)
        self.new_or.new_order_statr(browser)





if __name__ == '__main__':
    my = MyTestCase()

