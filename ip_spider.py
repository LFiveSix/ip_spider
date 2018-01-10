__author__ = 'HuaHua'

import urllib.request
import urllib.parse
import time, requests
from multiprocessing import Pool
import random
from lxml import etree
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
client = MongoClient('localhost', 27017)
db = client.ip


def change_Agent():
    agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
        ]
    agent = random.choice(agents)
    return agent


def get_ips():
    """
    爬取国内高匿代理IP
    [['110.73.5.226:8123'], ['118.72.124.97:80'], ['106.12.8.215:808'], ['123.185.130.121:8080'], ['112.114.96.196:8118'], ['125.113.101.3:808'], ['171.39.78.54:8123'], ['106.58.123.176:80'], ['112.114.76.61:8118'], ['112.114.76.233:8118'], ['110.73.41.141:8123'], ['112.114.95.69:8118']]
    """

    ips_list = []
    # 只爬取十页ip
    for page in range(1, 2):
        print("#####爬取第" + str(page) + "页#####")
        print("ip地址\t\t\t\t\t端口号\t\t\t存活时间\t验证时间")
        url = 'http://www.xicidaili.com/nn/' + str(page)
        agent = change_Agent()
        headers = ("User-Agent", agent)
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        try:
            web_data = opener.open(url, timeout=5).read()
            print(web_data)
        except Exception as e:
            print("爬取页面出错，错误为：", e)
        selector = etree.HTML(web_data)
        ip_address_s = selector.xpath('//tr[@class="odd"]/td[2]/text()')  # ip地址
        port_numbers = selector.xpath('//tr[@class="odd"]/td[3]/text()')  # 端口号
        survive_time = selector.xpath('//tr[@class="odd"]/td[9]/text()')  # 存活时间
        verify_time = selector.xpath('//tr[@class="odd"]/td[10]/text()')  # 验证时间
        ip_numbers = len(ip_address_s)
        for i in range(ip_numbers):
            ip = ip_address_s[i] + ":" + port_numbers[i]
            ips_list.append(ip)
            print(ip_address_s[i]+"\t\t\t\t\t"+port_numbers[i]+"\t\t\t"+survive_time[i]+"\t"+verify_time[i])
    return ips_list


def get_verify_ip(verify_ip):
    """
    验证网页ip是否可用
    """
    valid_ips = []
    target_url = 'http://2017.ip138.com/ic.asp'
    agent = change_Agent()
    # 使用代理
    proxy_support = urllib.request.ProxyHandler({"http": verify_ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [("User-Agent", agent)]
    urllib.request.install_opener(opener)
    try:
        res = requests.get(target_url, proxies={"http": verify_ip})
        print(res.status_code)
        response = urllib.request.urlopen(target_url, timeout=5).read()
        if len(response) != 0:
            valid_ips.append(verify_ip)
    except urllib.error.URLError as e2:
        if hasattr(e2, "code"):
            print("验证代理IP（"+verify_ip+"）发生HTTPError错误")
            print("错误原因："+str(e2.code))
        if hasattr(e2, "reason"):
            print("验证代理IP（"+verify_ip+"）发生URLError错误")
            print("错误原因："+str(e2.reason))
    except Exception as er:
        print("验证代理IP（"+verify_ip+"）时发生错误")
        print("错误为："+str(er))
    time.sleep(3)
    print("######:", valid_ips)
    return valid_ips


def mul_get_verify_ip(ips_list):
    """
    多进程验证ip有效性
    """
    pool = Pool(processes=7)
    fl_proxies = pool.map(get_verify_ip, ips_list)
    pool.close()
    pool.join()  # 等待进程池中的worker进程执行完毕
    print("!!!!!:", fl_proxies)
    return fl_proxies


def clear_valid_ip(valid_ips):
    #  整理可用IP
    verify_ip_address = []
    for valid_ip in valid_ips:
        if len(valid_ip) != 0:
            verify_ip_address.append(valid_ip)
    print(verify_ip_address)
    print("verify_ip_address长度：", len(verify_ip_address))
    return verify_ip_address


def save_ip_into_mongodb(verify_ip_address):
    for ip in verify_ip_address:
        db.ip.insert({"ip": ip})


if __name__ == '__main__':
    ips_list = get_ips()  # 获得网页ip
    valid_ips = mul_get_verify_ip(ips_list)
    verify_ip_address = clear_valid_ip(valid_ips)
    save_ip_into_mongodb(verify_ip_address)
    """
    定时
    # sched = BlockingScheduler()
    # sched.add_job(my_job, 'interval', seconds=5)
    # sched.start()
    """
