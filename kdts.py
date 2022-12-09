from sendemil import send
import requests
from os import environ
import time
def get_environ(key, default="", output=True):
    def no_read():
        if output:
            print(f"未填写环境变量 {key} 请添加")
        return default
    return environ.get(key) if environ.get(key) else no_read()
Province = get_environ("Province")
City = get_environ("City")
Area = get_environ("Area")
Address = get_environ("Address")
t = int(time.time())
url = 'https://www.kuaidi100.com/apicenter/order.do?method=expressStopInquiries'
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "177",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_gcl_au=1.1.105637400.{}; _ga=GA1.1.417363123.{}; _ga_RX03B5S2PX=GS1.1.{}.1.1.1670071368.46.0.0; _adadqeqwe1321312dasddocTitle=kuaidi100; _adadqeqwe1321312dasddocReferrer=; _adadqeqwe1321312dasddocHref=; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1670071354,1670132879,1670216039; WWWID=WWWF21B4E55B3CB6DA8542216F1163EA0E3; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1670224704".format(t,t,t,t,t),
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
'toProvince': '河北省',
'toCity': '沧州市',
'toArea': '南皮县',
'toAddress': '潞灌乡辛庄村'
}
kddict = requests.post(url=url,headers=headers,data=data).json()
print(kddict)
kdlist = kddict['data']['toReachable']
state = [{'快递':'圆通','状态':'','原因':''},{'快递':'申通','状态':'','原因':''},{'快递':'中通','状态':'','原因':''},{'快递':'韵达','状态':'','原因':''},{'快递':'极兔','状态':'','原因':''},{'快递':'德邦','状态':'','原因':''},{'快递':'京东','状态':'','原因':''},{'快递':'顺丰','状态':'','原因':''},{'快递':'邮政','状态':'','原因':''}]
for i in range(len(kdlist)):
    if kdlist[i]['reachable'] == 0:
        state[i]['状态'] = '停发'
        state[i]['原因'] = kdlist[i]['reason']
    else:
        state[i]['状态'] = '可达'
#print(state)
reach = '可达: '
stop = '停发: '
reachlist = []
stoplist = []
for i in state:
    if i['状态'] == '可达':
        reach = reach + i['快递'] + '  '
        reachlist.append(i['快递'])
    else:
        stop = stop + i['快递'] + '  ' + '原因: ' + str(i['原因']) + ' \n     '
        stoplist.append(i['快递'])
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

