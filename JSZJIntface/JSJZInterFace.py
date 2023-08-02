import requests

import Jsonformatting

"""
金租查询客户预审批结果
"""


class interface_jz_11():
    def __init__(self, ZD_JSJZ_CUSTOMER):
        self.ZD_JSJZ_CUSTOMER = ZD_JSJZ_CUSTOMER

    def jz_JFL_11(self):
        data_jz_11 = {"body": {"CUSTOMER_CODE": self.ZD_JSJZ_CUSTOMER}, "head": {"businessType": "JFL-11"}}
        r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_11)
        a = Jsonformatting.JsonFormat(r)
        a.JsonChange()


"""
金租查询客户签署合同状态
"""


class interface_jz_60():
    def __init__(self, CONT_NAME):
        self.CONT_NAME = CONT_NAME

    def jz_JFL_60(self):
        data_jz_60 = {"head": {"businessType": "JFL-60"}, "body": {"CONT_NAME": self.CONT_NAME}}
        r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_60)
        a = Jsonformatting.JsonFormat(r)
        a.JsonChange()


"""
金租交易新增结果查询
"""


class interface_jz_39():
    def __init__(self, PK_DEAL_APPLICATION, APPLICATION_CODE):
        self.PK_DEAL_APPLICATION = PK_DEAL_APPLICATION
        self.APPLICATION_CODE = APPLICATION_CODE

    def jz_JFL_39(self):
        data_jz_39 = {"head": {"businessType": "JFL-39"},
                      "body": {"PK_DEAL_APPLICATION": self.PK_DEAL_APPLICATION, "TYPE": 1,
                               "APPLICATION_CODE": self.APPLICATION_CODE}}
        r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_39)
        a = Jsonformatting.JsonFormat(r)
        a.JsonChange()


"""
金租还款卡确认 
"""


class interface_jz_55():
    def __init__(self, CONT_NAME, CUSTOMER_CODE, ACCOUNT_NO):
        self.CONT_NAME = CONT_NAME
        self.CUSTOMER_CODE = CUSTOMER_CODE
        self.ACCOUNT_NO = ACCOUNT_NO

    def jz_JFL_55(self):
        data_jz_55 = {"head": {"businessType": "JFL-55"},
                      "body": {"CONT_NAME": self.CONT_NAME, "CUSTOMER_CODE": self.CUSTOMER_CODE,
                               "ACCOUNT_NO": self.ACCOUNT_NO, "TYPE": "1"}}
        r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_55)
        a = Jsonformatting.JsonFormat(r)
        a.JsonChange()


class interface_jz_56():
    def __init__(self, BANK_TYPE, CUSTOMER_CODE, ACCOUNT_NO, MOBILE):
        self.BANK_TYPE = BANK_TYPE
        self.CUSTOMER_CODE = CUSTOMER_CODE
        self.ACCOUNT_NO = ACCOUNT_NO
        self.MOBILE = MOBILE
    # 银行分类 BANK_TYPE 银行分类，1：中国工商银行，2：中国农业银行，3：邮储银行，7：交通银行

    def jz_JFL_56(self):
        data_jz_56 = {"head": {"businessType": "JFL-56"},
                      "body": {"BANK_TYPE": self.BANK_TYPE, "CUSTOMER_CODE": self.CUSTOMER_CODE, "ACCOUNT_NO": self.ACCOUNT_NO,
                               "MOBILE": self.MOBILE}}
        r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_56)
        a = Jsonformatting.JsonFormat(r)
        a.JsonChange()





