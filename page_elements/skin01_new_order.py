#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.page_base import Basepage

class skin01_new_order(Basepage):

    createOrderBtn = 'id=>createOrderBtn' # 新建订单

    # receiverName = 'name=>receiverName' #收件人
    receiverName = 'x=>//*[@id="createOrderTPL"]/form/div[1]/div[2]/div[2]/div[1]/input'
    receiverPhone = 'name=>receiverPhone' #电话
    receiverMobile = 'name=>receiverMobile' #手机
    province = 'name=>province' #省
    city = 'name=>city' #市
    district = 'name=>district' #区
    receiverAddress = 'id=>address' #详细地址
    sellerMessage = 'name=>sellerMessage' #备注信息
    goodsNo = 'name=>goodsNo' #商品编码
    goodsName = 'x=>//*[@id="goodsInfoBody"]/tr/td[3]/input' #商品标题
    goodsProps = 'name=>goodsProps' #商品属性
    quantity = 'x=>//*[@id="goodsInfoBody"]/tr/td[5]/input' #商品数量
    price = 'name=>price' #单价

    confirmCreateOrder = 'x=>//*[@id="createOrderTPL"]/form/div[2]/a[1]' #保存
    Save_tip = 'x=>html/body/div[9]' #保存提示
    Save_tip_button = 'x=>/html/body/div[9]/div[7]/div/button' #确认
    error_tip = 'id=>tip' # 新建订单的错误提示


    def new_order(self,browser,order_info):
        self.click(self.createOrderBtn)
        self.sleep(2)
        # div = self.find_element(self.new_order_div)
        self.input(self.receiverName,order_info[0])
        self.input(self.receiverPhone, order_info[1])
        self.input(self.receiverMobile, order_info[2])
        self.input(self.province, order_info[3])
        self.input(self.city, order_info[4])
        self.input(self.district, order_info[5])
        self.input(self.receiverAddress, order_info[6])
        self.input(self.sellerMessage, order_info[7])
        self.input(self.goodsNo, order_info[8])
        self.input(self.goodsName, order_info[9])
        self.input(self.goodsProps, order_info[10])
        self.input(self.quantity, order_info[11])
        self.input(self.price, order_info[12])
        self.click(self.confirmCreateOrder)


    def new_order_tip(self):
        Save_tip_statu = self.element_is_dispalynd(self.Save_tip)
        if Save_tip_statu!=False:
            Save_tip = self.get_elemeent_text(self.Save_tip)
            if '新建订单成功' in Save_tip:
                self.click(self.Save_tip_button)
                return True
            else:
                # if self.element_is_dispalynd(self.Save_tip_button)
                # self.click(self.Save_tip_button)
                return False
        else:
            return None


    def new_error_tip(self):
        errpr_tip = self.element_is_dispalynd(self.error_tip)
        if errpr_tip!=False:
            tip = self.get_elemeent_text(self.Save_tip)
            if len(tip)==0:
                return False
            else:
                return tip
        else:
            return False



