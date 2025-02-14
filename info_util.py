import datetime
import random

import requests
import json

base_path = "/Users/Coki_Zhao/Desktop/soft/data/"

class CircularQueue:
    def __init__(self, maxsize):
        self.queue = []
        self.maxsize = maxsize

    def put(self, item):
        if len(self.queue) == self.maxsize:
            # 移除最早的元素
            self.queue.pop(0)
        # 添加新元素
        self.queue.append(item)

    def get_all(self):
        return self.queue

class InfoUtil:
    def __init__(self):
        # 实例化 CircularQueue
        self.gold_queue = CircularQueue(24)
        self.rate_queue = CircularQueue(24)
        self.time_queue = CircularQueue(24)
        # we need call the api to update the data every hour, so we need to record the last hour
        self.old_hour = ""

    def update_if_need(self):
        # check the queue is null, then we need to update
        if len(self.gold_queue.get_all()) == 0:
            self.update_exchange_rate()
            self.update_gold_info()
        else:
            new_hour = datetime.datetime.now().strftime('%H')
            if new_hour != self.old_hour:
                minute = datetime.datetime.now().strftime('%M')
                if minute == "16":
                    self.update_exchange_rate()
                    self.update_gold_info()
                    # update the old hour
                    self.old_hour = new_hour


    def update_exchange_rate(self):
        # 基本参数配置
        apiUrl = 'http://op.juhe.cn/onebox/exchange/currency'  # 接口请求URL
        apiKey = 'xxxxxxxxx'  # 在个人中心->我的数据,接口名称上方查看

        # 接口请求入参配置
        requestParams = {
            'key': apiKey,
            'from': 'USD',
            'to': 'CNY ',
            'version': '',
        }

        # 发起接口网络请求
        response = requests.get(apiUrl, params=requestParams)

        # 解析响应结果
        if response.status_code == 200:
            res_json = response.json()
            with open(base_path + 'exchange_rate.txt', 'a') as file:
                file.write(json.dumps(res_json['result'][0]) + "\n")
            self.rate_queue.put(res_json['result'][0]['exchange'][:-5])
        else:
            # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
            print('请求异常')

    def update_gold_info(self):
        # 基本参数配置
        apiUrl = 'http://web.juhe.cn/finance/gold/shgold'  # 接口请求URL
        apiKey = 'xxxxxxxxx'  # 在个人中心->我的数据,接口名称上方查看

        # 接口请求入参配置
        requestParams = {
            'key': apiKey,
            'v': '',
        }

        # 发起接口网络请求
        response = requests.get(apiUrl, params=requestParams)

        # 解析响应结果
        if response.status_code == 200:
            res_json = response.json()
            with open(base_path + 'gold.txt', 'a') as file:
                file.write(json.dumps(res_json['result'][0]) + "\n")
            self.gold_queue.put(res_json['result'][0]['4']['latestpri'])
            self.time_queue.put(res_json['result'][0]['4']['time'][8:13].replace(" ", "-"))
        else:
            # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
            print('请求异常')


# s = "{'reason': '查询成功!', 'result': [{'currencyF': 'USD', 'currencyF_Name': '美元', 'currencyT': 'CNY', 'currencyT_Name': '人民币', 'currencyFD': '1', 'exchange': '7.30520000', 'result': '7.30520000', 'updateTime': '2025-02-10 15:15:27'}, {'currencyF': 'CNY', 'currencyF_Name': '人民币', 'currencyT': 'USD', 'currencyT_Name': '美元', 'currencyFD': '1', 'exchange': '0.13689000', 'result': '0.13689000', 'updateTime': '2025-02-10 15:15:27'}], 'error_code': 0}"
# j = json.loads(s.replace("'", '"'))
# print(j['result'][0])


# s = "{'resultcode': '200', 'reason': 'SUCCESSED!', 'result': [{'1': {'variety': 'Au100g', 'latestpri': '679.88', 'openpri': '668.0', 'maxpri': '680.0', 'minpri': '668.0', 'limit': '1.47%', 'yespri': '670.00', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '2': {'variety': 'Au(T+N1)', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': 'NaN%', 'yespri': '-', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '3': {'variety': 'Au(T+D)', 'latestpri': '679.17', 'openpri': '669.0', 'maxpri': '679.17', 'minpri': '666.36', 'limit': '1.59%', 'yespri': '668.56', 'totalvol': '49752.00', 'time': '2025-02-10 15:44:31'}, '4': {'variety': 'Au99.99', 'latestpri': '679.8', 'openpri': '669.0', 'maxpri': '679.99', 'minpri': '666.0', 'limit': '1.62%', 'yespri': '668.99', 'totalvol': '1249.00', 'time': '2025-02-10 15:44:31'}, '5': {'variety': 'Au99.95', 'latestpri': '688.0', 'openpri': '668.9', 'maxpri': '688.0', 'minpri': '668.9', 'limit': '2.85%', 'yespri': '668.96', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '6': {'variety': 'Au50g', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': 'NaN%', 'yespri': '--', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '7': {'variety': 'Ag99.99', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '-', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '8': {'variety': 'Ag(T+D)', 'latestpri': '8041.0', 'openpri': '8029.0', 'maxpri': '8122.0', 'minpri': '7985.0', 'limit': '0.27%', 'yespri': '8019.00', 'totalvol': '411582.00', 'time': '2025-02-10 15:44:31'}, '9': {'variety': 'Au(T+N2)', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '-', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '10': {'variety': 'Pt99.95', 'latestpri': '239.11', 'openpri': '237.66', 'maxpri': '239.11', 'minpri': '237.66', 'limit': '-0.28%', 'yespri': '239.79', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '11': {'variety': 'AU995', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '370.50', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '12': {'variety': 'AU99.99', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '643.10', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '13': {'variety': 'MAUTD', 'latestpri': '679.3', 'openpri': '669.0', 'maxpri': '679.3', 'minpri': '666.58', 'limit': '1.59%', 'yespri': '668.65', 'totalvol': '111322.00', 'time': '2025-02-10 15:44:31'}, '14': {'variety': 'IAU99.99', 'latestpri': '678.81', 'openpri': '670.78', 'maxpri': '678.81', 'minpri': '670.0', 'limit': '1.26%', 'yespri': '670.34', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '15': {'variety': 'IAU100G', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '-', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}, '16': {'variety': 'IAU99.5', 'latestpri': '--', 'openpri': '--', 'maxpri': '--', 'minpri': '--', 'limit': '--', 'yespri': '-', 'totalvol': '--', 'time': '2025-02-10 15:44:31'}}], 'error_code': 0}"
# j = json.loads(s.replace("'", '"'))
# print(j['result'][0]['4'])

# util = InfoUtil()
# util.update_exchange_rate()