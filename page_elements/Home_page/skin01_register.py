#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.page_base import Basepage


class skin01_register(Basepage):
    #------------------------验证手机元素---------------------------------#
    mobile = 'id=>mobile' #手机号码
    captchaImg1 = 'id=>captchaImg1' #验证码图片
    captcha1 = 'id=>captcha1' #验证码输入框
    checkCodeMobile='id=>checkCodeMobile' # 短信验证码输入框
    sendMobileCodeBtn = 'id=>sendMobileCodeBtn' #短信验证码发送
    codeTip = 'id=>codeTip' #信息提示
    regBtn01 = 'id=>regBtn01' #下一步
    # -------------------------------------------------------------------#


    # ------------------------设置密码元素---------------------------------#
    loginName = 'id=>loginName' #账号
    pwd = 'id=>pwd' #密码
    captcha2 = 'id=>captcha2' #验证输入框
    captchaImg2 = 'id=>captchaImg2' #验证码图片
    regBtn02 = 'id=>regBtn02' #注册
    backBtn = 'id=>backBtn' #上一步
    sf_dialog = 'id=>sf_dialog' #提示框
    sf_dialog_textdiv = 'x=>//*[@id="sf_dialog"]/div[2]' #提示框的子框
    # -------------------------------------------------------------------#

    # ------------------------注册完成元素---------------------------------#
    login_button = 'x=>//*[@id="regComplete"]/div[2]/a/label'
    # -------------------------------------------------------------------#


    # ------------------------验证手机方法---------------------------------#
    # 验证手机
    def Verifying_mobile(self,mobile):

        self.input(self.mobile,mobile)
        captcha1 = input('请输入图片验证码：')
        self.input(self.captcha1,captcha1)
        self.click(self.sendMobileCodeBtn)
        self.sleep(0.5)
        code = input('请输入短信验证码：')
        self.input(self.checkCodeMobile,code)
        self.click(self.regBtn01)

    def send_mobile(self,mobile):
        self.clear(self.mobile)
        self.input(self.mobile, mobile)

    def send_captcha1(self):
        self.clear(self.mobile)
        captcha1 = input('请输入图片验证码：')
        self.input(self.mobile, captcha1)

    def send_checkCodeMobile(self,checkCodeMobile):
        self.clear(self.mobile)
        self.click(self.sendMobileCodeBtn)
        checkCodeMobile = input('请输入短信验证码：')
        self.input(self.mobile, checkCodeMobile)


    # 判断是否有提示信息
    def get_error_tip(self):
        statu = self.element_is_dispalynd(self.codeTip)
        if statu:
            elemeent_text = self.get_elemeent_text(self.codeTip)
            return elemeent_text
        else:
            return None

    #点击验证码图片
    def click_captchaImg1(self):
        self.click(self.captchaImg1)

    #点击发送短信验证码按钮
    def click_sendMobileCodeBtn(self):
        self.click(self.sendMobileCodeBtn)

    # -------------------------------------------------------------------#

    # ------------------------设置密码方法---------------------------------#
    def Set_password(self,loginName,password):
        self.clear(self.loginName)
        self.clear(self.pwd)
        self.clear(self.captcha2)

        self.input(self.loginName,loginName)
        self.input(self.pwd,password)
        code = input('请输入验证码：')
        self.input(self.captcha2,code)
        self.click(self.regBtn02)

    # 获取提示
    def get_tip(self):
        statu = self.element_is_dispalynd(self.sf_dialog)
        if statu:
            elemeent_text = self.get_elemeent_text(self.sf_dialog_textdiv)
            return elemeent_text
        else:
            return None
    # -------------------------------------------------------------------#


    # ------------------------验证手机方法---------------------------------#
    def click_loginbutton(self):
        self.click('login_button')
        self.sleep(2)