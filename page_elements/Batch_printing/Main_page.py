#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.page_base import Basepage

class main_page(Basepage):

    topNavBtn = 'id=>topNavBtn' # 个人信息
    logoutBtn = 'id=>logoutBtn' # 退出系统

    def out_system(self):
        try:
            self.Mouse_suspension(self.topNavBtn)
            self.sleep(1)
            self.click(self.logoutBtn)
        except:
            pass


