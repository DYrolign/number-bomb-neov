import json


# API
class api:
    # 获取数据
    def getConfig(path):
        # current_path = os.path.dirname(__file__)
        with open(path + '.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data

    # 获取信息
    def getMsg(message):
        lg = api.getConfig('settings')['lang']
        lang = api.getConfig("lang\\"+lg)
        msg = lang[message]
        return msg
