import requests
import os
import json






def check_ip(ip):
    headers = {"User-Agent": "curl/1.17"}
    url = 'https://ip.useragentinfo.com/json?ip={}'.format(ip)
    response = requests.get(url=url,headers=headers)
    date = json.loads(response.text)
    return date["ip"], date["province"],  date["isp"]


# print(check_ip("120.232.249.5"))



# 获取serverIP
def get_server_ip(ip, domain):
    ip_list = []
    os.system(f"dig +subnet={ip} {domain} @119.29.29.29 +short A |grep -v '[a-z]' >{ip}.log")
    for line in open(f"{ip}.log", "r"):
        rs = line.rstrip('\n')
        ip_list.append(rs)
    os.remove(f"{ip}.log")
    return ip,  ip_list

# 获取客户端IP 和服务端IP的省份运营商，返回两个列表client_isp 和 server_isp
def get_all_isp(ip, domain):
    a = get_server_ip(ip, domain)
    clinetIP = a[0]
    serverIP = a[1]
    server_isp = []
    clinet_isp = check_ip(clinetIP)
    for i in serverIP:
        server_isp.append(check_ip(i))
    return clinet_isp, server_isp

# print(get_all_isp("120.232.249.5", "www.baidu.com"))

# 判断客户端IP 和服务端IP 省份运营商情况
"""
把客户端IP和serverIP组合成一个元组，然后对这个元组进行分析，判断serverIP 和clientIP是否是相同的省份运营商
分成5中情况：
1.是相同省份运营商；
2.是相同运营商，但是不是相同省份，此时需要给出明显的提示，不是本省运营商覆盖
3.不是相同运营商，如果不是相同运营商，此时需要给出明显的提示，跨运营商覆盖，可能影响访问效果；
4.部分是本地运营商，部分是外省运营覆盖，此时需要给出明显的提示，并给出本地运营商占比；
5.部分是相同运营商，部分非相同运营商，此时需要给出明显提示，这个省份的运营商覆盖存在跨运营商覆盖，可能影响访问；

针对这五种情况，需要给出一个函数，自动判定情况，给出相关结论
judge_coverage函数还需要完善判断规则，完善后才能更好的判断，当前print函数会打印多次。

"""



def judge_coverage(ip, domain):
    b = get_all_isp(ip, domain)
    client_isp = b[0]
    server_isp = b[1]
    for i in range(len(server_isp)):
        if client_isp[2] != server_isp[i][2]:
            print(client_isp[1], client_isp[2], "客户端IP：", client_isp[0], "当前跨运营商覆盖，请检查服务端覆盖！服务端IP运营商:", server_isp[i])
        elif client_isp[1] != server_isp[i][1]:
            print(client_isp[1] ,client_isp[2], "相同运营商，非本地覆盖，请检查服务端覆盖！")
        else:
            print(client_isp[1], client_isp[2], "本地覆盖")

"""
从文件中获取客户端IP ，传递给到主函数或者给到judge_coverage函数中。

"""


def main(domain):
    for line in  open('ip.list', 'r'):
        rs = line.rstrip('\n')
        judge_coverage(rs, domain)


if __name__  ==  '__main__' :
    main("m.360buyimg.com")


