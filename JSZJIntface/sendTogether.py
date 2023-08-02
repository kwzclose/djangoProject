

import JSJZInterFace as se




# 金租查询客户预审批结果
a= se.interface_jz_11('2202328401000').jz_JFL_11()
#
# print("-----------------不同接口的分割线----------------------------------------------------")
# # 金租查询客户签署合同状态
# b= se.interface_jz_60('JFL23P03L007742-01').jz_JFL_60()
# 金租交易新增结果查询
# select  from ZD_JSJZ_LOAN z where z.CONTRACT_ID =(select c.CONTRACT_ID from con_contract c where c.CONTRACT_NUMBER='CON230400042' and c.DATA_CLASS='NORMAL');
# c=se.interface_jz_39('0001AA10000000NP9Y92','P2304060092').jz_JFL_39()
# 金租还款卡确认
# d=se.interface_jz_55('JFL23P03L013700-01','22021109881000','6212261901015279688').jz_JFL_55()
# 金租还款卡四要素验证接口
# f=se.interface_jz_56('1','22021109881000','6212261901015279688','13677353701').jz_JFL_56()


