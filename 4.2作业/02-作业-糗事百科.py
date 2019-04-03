import urllib.request
import time
import re


# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)


def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    }

    req = urllib.request.Request(url, headers=headers)
    # 获取服务器响应数据
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    # print(html)
    name_re = "<h2>(.*?)</h2>"
    coms = re.compile(name_re, re.S)
    name_str = coms.findall(html)
    # print(strs)
    content_re = "<span>\n\n(.*?)</span>"
    con = re.compile(content_re, re.S)
    content_str = con.findall(html)
    return name_str, content_str


if __name__ == "__main__":
    # 所有数据
    allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # # 遍历每一页的数据
    for i in range(1,4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        allData.extend(list1)
        time.sleep(0.5)
     # 遍历allData 把数据显示
    for j in range(len(allData)):
        if not j %2:
            for i in range(len(allData[j])):
                print("%s 说： %s\n" % (
                allData[j][i].strip('\n'), allData[j+1][i].strip('\n')))

