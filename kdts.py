from sendemil import send
import requests
from os import environ
import time
import re
def get_environ(key, default="", output=True):
    def no_read():
        if output:
            print(f"未填写环境变量 {key} 请添加")
        return default
    return environ.get(key) if environ.get(key) else no_read()
def login(name,password):
    url = 'https://sso.kuaidi100.com/pcweb/login/accountlogin'
    headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }

    data = {
    "directlogin": "1",
    "data": "JofmxldwnAX71Q7rDGGQHNs5anPRdwPzuv2NkcffIWdlY6FYbTlru2N-Y836XmHETkGJCM_dRxenPPlUTGhBTEWR2DFYlbvc0p4_fqyOfbI-PT7TnynbzL5ZSiMMcD4MN6YhvZC_uzPqvG4ePERrcq7BDHARirNuDEduYyS_PZGDAmrg15odEBAvMBe6nytdNFIxzcZiKnNahkgHd9qkKHJ9lhTkvIjZ",
    "sign": "3A3773A439D9E82821FE1EBB2787A870",
    'name': name,
    'password': password
    }
    k = requests.post(url=url, headers=headers, data=data)
    #print(k.request.headers)

    token = re.split('TOKEN=|;', k.request.headers['Cookie'])[2]
    #print(token)
    return token
def sent(content,token):
    url = 'https://www.kuaidi100.com/market/open/sent.do'
    headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Content-Length":"294",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    #"Cookie":'ngxto=kd-market-7d77f8fcdf-k4csw; _adadqeqwe1321312dasddocReferrer=; _adadqeqwe1321312dasddocHref=; loginEmail=; WWWID=WWW985DF8E09658DF17234B50B025A8828E; _adadqeqwe1321312dasddocTitle=kuaidi100; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1670071354,1670132879,1670216039,1670555038; DEVICE_NUM=e26f26a1e6914cfebbdb3ade742d1050; SELF_TOKEN=PI2C09_f91415bf61b44b4189d5b50c85ba57ea; TOKEN=bHilxpGqw7bD3TWVuRWci8wEcJGGx6lxd3QJZ86giyM; loginId=629802775; loginType=BUYER; loginName=15132723127; nickname=15132723127; loginMobile=15132723127; loginExt={}; auth=1; loginSession=1; _gcl_au=1.1.1208616931.1670558183; _ga=GA1.1.1338221575.1670558183; _ga_RX03B5S2PX=GS1.1.1670558183.1.0.1670558188.55.0.0; __bid_n=184f4f89f5b45c20354207; FEID=v10-febf70322a86d550fa35bc6bef846033d04b54e9; __xaf_fpstarttimer__=1670558203236; __xaf_ths__={"data":{"0":1,"1":86400,"2":60},"id":"57f9db7e-1f86-450b-91e3-1d9d59322c9e"}; __xaf_thstime__=1670558203337; FPTOKEN=h+JcDpP14+1Tzb8HDOI8O67JI2AepL4ZIp/L6Ht075SErrJZ2tfUcnlcCm11xl4z5c6adKAx85p+4/t/ZePtCLT0Olbs9YANtve5AlLYxO8c8OF1l3ZfDr3s1beeMJ2ggzj2IdO72bunbk2E87cvcUtcMBN3ae7bg/nCYAUf1Rp2qnNQ8zLoeigXDaURdIYoEJCgs7AP+Gh7FkDOSwJLY7JCfknWPvXXKhcLvp5TEN0pbbVNhPCoSD7NX/ej16Ir/37bMs1Idi+u7M8nfAfJUv5oIB01zB+zyOLWM0/1aTITO0cB9zzgyTnVZnVcSVSHaGNM/9JGjfFU1q1CWExYdJM0OoIBcfyv8KL/fHxdoyljEy+VwenWobOWv5YeiYudajfvnh1l0XXuq1iRsVF8kQ==|1975ubQxbo0hABi6su4U8NIbH/YyjfVXEQbuj4/RqrI=|10|9392d8fd3a7be03db17661b66cd2cbfb; __xaf_fptokentimer__=1670558203439; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1670559072',
    "Host":"www.kuaidi100.com",
    "Origin":"https://www.kuaidi100.com",
    "Referer":"https://www.kuaidi100.com/stop/stop.jsp",
    "sec-ch-ua":"\"Not?A_Brand\";v=\"8\",\"Chromium\";v=\"108\",\"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
    data = {
      'method': 'infosplit',
      'content': content,
      'token': token
    }
    sentdict = requests.post(url=url, headers=headers, data=data).json()
    if sentdict["status"] == "200":
        sentlists = sentdict['data'][0]["xzq"]
        province = sentlists['province']
        city = sentlists['city']
        district = sentlists['district']
        subArea = sentlists['subArea']
        return province,city,district,subArea
def main():
    content = get_environ("content")
    name = get_environ("name")
    password = get_environ("password")
    token = login(name,password)
    addturple = sent(content,token)
    Province = addturple[0]
    City = addturple[1]
    Area = addturple[2]
    Address = addturple[3]
    url = 'https://www.kuaidi100.com/apicenter/order.do?method=expressStopInquiries'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "177",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        #"Cookie": 'Cookie: _adadqeqwe1321312dasddocReferrer=; _adadqeqwe1321312dasddocHref=; loginEmail=; WWWID=WWW985DF8E09658DF17234B50B025A8828E; _adadqeqwe1321312dasddocTitle=kuaidi100; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1670071354,1670132879,1670216039,1670555038; DEVICE_NUM=e26f26a1e6914cfebbdb3ade742d1050; SELF_TOKEN=PI2C09_f91415bf61b44b4189d5b50c85ba57ea; TOKEN=bHilxpGqw7bD3TWVuRWci8wEcJGGx6lxd3QJZ86giyM; loginId=629802775; loginType=BUYER; loginName=15132723127; nickname=15132723127; loginMobile=15132723127; loginExt=%7B%7D; auth=1; loginSession=1; _gcl_au=1.1.1208616931.1670558183; _ga=GA1.1.1338221575.1670558183; _ga_RX03B5S2PX=GS1.1.1670558183.1.0.1670558188.55.0.0; __bid_n=184f4f89f5b45c20354207; FEID=v10-febf70322a86d550fa35bc6bef846033d04b54e9; __xaf_fpstarttimer__=1670558203236; __xaf_ths__={"data":{"0":1,"1":86400,"2":60},"id":"57f9db7e-1f86-450b-91e3-1d9d59322c9e"}; __xaf_thstime__=1670558203337; FPTOKEN=h+JcDpP14+1Tzb8HDOI8O67JI2AepL4ZIp/L6Ht075SErrJZ2tfUcnlcCm11xl4z5c6adKAx85p+4/t/ZePtCLT0Olbs9YANtve5AlLYxO8c8OF1l3ZfDr3s1beeMJ2ggzj2IdO72bunbk2E87cvcUtcMBN3ae7bg/nCYAUf1Rp2qnNQ8zLoeigXDaURdIYoEJCgs7AP+Gh7FkDOSwJLY7JCfknWPvXXKhcLvp5TEN0pbbVNhPCoSD7NX/ej16Ir/37bMs1Idi+u7M8nfAfJUv5oIB01zB+zyOLWM0/1aTITO0cB9zzgyTnVZnVcSVSHaGNM/9JGjfFU1q1CWExYdJM0OoIBcfyv8KL/fHxdoyljEy+VwenWobOWv5YeiYudajfvnh1l0XXuq1iRsVF8kQ==|1975ubQxbo0hABi6su4U8NIbH/YyjfVXEQbuj4/RqrI=|10|9392d8fd3a7be03db17661b66cd2cbfb; __xaf_fptokentimer__=1670558203439; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1670558211',
        "Host": "www.kuaidi100.com",
        "Origin": "https://www.kuaidi100.com",
        "Referer": "https://www.kuaidi100.com/stop/stop.jsp",
        "sec-ch-ua": "\"Google Chrome\";v=\"107\",\"Chromium\";v=\"107\",\"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site":"same-origin",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }

    data = {
    'method': 'expressStopInquiries',
    'platform': 'WWW',
    'toProvince':Province,
    'toCity': City,
    'toArea': Area,
    'toAddress': Address,
    'sendxzq': Province+City,
    'token': token
    }
    kddict = requests.post(url=url,headers=headers,data=data).json()
    #print(kddict)
    kdlist = kddict['data']['toReachable']
    state = {"zhongtong":{'快递':'中通','状态':'','原因':''},"shentong":{'快递':'申通','状态':'','原因':''},"yuantong":{'快递':'圆通','状态':'','原因':''},"yunda":{'快递':'韵达','状态':'','原因':''},"jtexpress":{'快递':'极兔','状态':'','原因':''},"debangkuaidi":{'快递':'德邦','状态':'','原因':''},"jd":{'快递':'京东','状态':'','原因':''},"shunfeng":{'快递':'顺丰','状态':'','原因':''},"youzhengguonei":{'快递':'邮政','状态':'','原因':''}}
    for i in range(len(kdlist)):
        if kdlist[i]['reachable'] == 0:
            state[kdlist[i]["expressCode"]]['状态'] = '停发'
            state[kdlist[i]["expressCode"]]['原因']= kdlist[i]['reason']
        else:
            state[kdlist[i]["expressCode"]]['状态'] = '可达'
    #print(state)
    reach = '可达: '
    stop = '停发: '
    reachlist = []
    stoplist = []
    state = dict(state)
    #print(state)
    for i in state:
        if state[i]['状态'] == '可达':
            reach = reach + state[i]['快递'] + '  '
            reachlist.append(state[i]['快递'])
        else:
            stop = stop + state[i]['快递'] + '  ' + '原因: ' + str(state[i]['原因']) + ' \n     '
            stoplist.append(state[i]['快递'])
    #print(reach)
    #print(stop)
    result = str({'可达':reachlist,'停发':stoplist})
    file = open('config.txt', mode='r+',encoding='utf-8')
    file.seek(0,0)
    oldstr = file.read()
    #print(oldstr)
    if  oldstr == result:
        #print('xiangtong')
        file.close()
    else:
        #print(file.read())
        #print('butong')
        file.seek(0,0)
        file.write(result)
        file.close()
        send(reach + '\n' + stop)
if __name__ == '__main__':
     main()