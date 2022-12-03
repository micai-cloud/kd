from sendemil import send
import requests
from os import environ
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
url = 'https://www.kuaidi100.com/apicenter/order.do?method=expressStopInquiries'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400',
}
data = {
'method': 'expressStopInquiries',
'platform': 'WWW',
'toProvince': Province,
'toCity': City,
'toArea': Area,
'toAddress': Address
}
kddict = requests.post(url=url,headers=headers,data=data).json()
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

