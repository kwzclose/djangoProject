import json
import requests

class JsonFormat(object):

    def __init__(self,strtest):
        self.strtest = strtest


    def JsonChange(self):

        json_dic = json.loads(self.strtest.text)
        # 自动格式化打json格式
        j = json.dumps(json_dic, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
        print(j)


# data_jz_60 = {"head": {"businessType": "JFL-60"}, "body": {"CONT_NAME": "JFL23P03L010067-01"}}
#
# r = requests.post('http://192.168.100.49:18001/api/service/jsfl/send', json=data_jz_60)
# a=JsonFormat(r)
# a.JsonChange()