import urllib.request
import json
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

# from: zh
# to: en
# query: 你好
# transtype: realtime
# simple_means_flag: 3
# sign: 232427.485594
# token: 01792b0943eefc5b8a0fbef61af7d  2f6

url = 'https://fanyi.baidu.com/transapi'
englist = 'hello'

data = {
    'query': englist,
    'from': 'en',
    'to': 'zh',
    'transtype': 'realtime',
    'simple_means_flag': 3,
    'token': '01792b0943eefc5b8a0fbef61af7d2f6',
}
response = requests.post(url,data=data,headers=headers)
# print(response.status_code)
# print(response.text)
# print(response)
json_str = response.json()
res = json_str['data'][0]['result'][0][1]
print(res)
