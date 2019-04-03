# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"
import json
import urllib.request
import urllib.parse

def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
     }
    req = urllib.request.Request(url,headers=headers)
    responses = urllib.request.urlopen(req)
    content = responses.read().decode()
    content_list =json.loads(content)
    for con in content_list:
        img_url = con['cover_url']
        filename = con['title']
        # print(img_url)
        urllib.request.urlretrieve(img_url, filename='img/%s.jpg' %filename)

if __name__ == "__main__":

    for i in range(1, 3):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"

        getData(url)











