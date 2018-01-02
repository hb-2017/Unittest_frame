#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.page_base import Basepage


class skin01_user_login(Basepage):

    # 账户名,密码，记住密码，登录
    username = 'id=>userName'
    password = 'id=>passWord'
    remember_password = 'id=>remeber'
    sumbit = 'id=>submit'

    # 错误信息，验证码图片，验证码输入
    error_tips = 'id=>error_tips'
    captchaImg = 'id=>captchaImg'
    captcha = 'id=>captcha'

    #第三方登录按钮
    taobaoLogin = 'id=>taobaoLogin'
    qqLogin = 'id=>qqLogin'
    weixinLogin = 'id=>weixinLogin'

    #注册,忘记密码
    free_reg = 'id=>free_reg'
    forget_pwd = 'id=>forget_pwd'


    #输入账号密码
    def input_userinfo(self,username,password):
        self.input(self.username,username)
        self.input(self.password,password)

    #点击登录
    def click_login(self):
        self.click(self.sumbit)
        self.sleep(2)

    #获取错误信息并返回
    def get_error_tips(self):
        element = self.find_element(self.error_tips)
        element_text = element.text
        return element_text

    # 输入验证码
    def input_code(self):
        code = input('请输入登录图片验证码')
        self.input(self.captcha,code)



class taobao_login(Basepage):

    # 切换登录
    J_Static2Quick = 'id=>J_Static2Quick'  # 快速登录
    J_Quick2Static = 'id=>J_Quick2Static'  # 账号密码登录

    # 授权登录
    J_SubmitStatic = 'id=>J_SubmitStatic'

    # 账号是否登录
    taobaologin_statu_ = 'x=>/html/body/div/div[2]/div[1]/h3'

    # 账号，密码
    TPL_username_1 = 'id=>TPL_username_1'
    TPL_password_1 = 'id=>TPL_password_1'

    # 输入账号密码
    def input_taobaoinfo(self, username, password):
        self.browser.switch_to.frame("J_loginIframe")
        self.clear(self.TPL_username_1)
        self.clear(self.TPL_password_1)
        self.input(self.TPL_username_1, username)
        self.input(self.TPL_password_1, password)

    # 判断是否登录了淘宝
    def taobaologin_statu(self):
        tb_statu = self.element_is_dispalynd(self.taobaologin_statu_)
        return tb_statu