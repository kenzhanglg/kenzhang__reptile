from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

def content_data(url):
    href_list = []
    jobs_datas = []
    req = urllib.request.Request(url, headers=headers)
    responses = urllib.request.urlopen(req)
    content = responses.read()
    soup = BeautifulSoup(content, 'lxml')
    datas = soup.find_all('tr', class_=['even', 'odd'])
    # print(datas)
    for data in datas:
        href_con = data.select('td > a')[0]['href']
        href = 'https://hr.tencent.com/' + href_con
        href_list.append(href)
        da = data.text
        jobs_datas.append(da)
    return href_list,jobs_datas

def job_data(url):
    job_urls = content_data(url)[0]
    for i in range(len(job_urls)):
        req = urllib.request.Request(job_urls[i], headers=headers)
        responses = urllib.request.urlopen(req)
        content = responses.read()
        soup = BeautifulSoup(content, 'lxml')
        datas = soup.find_all('ul',class_='squareli')
        print(content_data(url)[1][i])
        print('工作职责：\n %s'%datas[0].text)
        print('工作要求：\n%s'%datas[1].text)
        print('*********************************')

if __name__ == '__main__':
    #页数
    for i in range(5):
        url = 'https://hr.tencent.com/position.php?keywords=python&lid=2218&start=%d#a'%(i*10)
        job_data(url)
