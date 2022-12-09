调用快递100停发接口，来查询当地快递能否到达。


本意是自用

使用github action定时执行，每小时查询一次。然后通过邮件发送到你的邮箱。欢迎fork和star.

推荐大家也使用github action，毕竟免费。
步骤如下:
fork以后回到自己的仓库，找到刚刚复制的我的仓库，点击Setting-、往下滑找到Secrets-Actions,点击它。然后点击new repository secert.
这时候出现两行，一个是Name,另一个是Secret.
Name里面填写变量名，Secret里面填写变量值.
 |序号|    Name       |   Secret|
|----| -----| -----|
|1| content      | xx省xx市xx县xx街道xx小区xx号(也就是把平时网购的地址写在这里)|
|2| name     | 手机号(需要去快递100注册一个账号，账号就是手机号)|
|3| password     | 密码(需要去快递100注册一个账号，密码在8位以上)|
|4| receiver     | 接收消息的邮箱，例如xxxxxxxxxx@qq.com或者xxxxxx@163.com|
添加一个变量名，然后添加对应的变量值，再点击add secrets.所以四个变量，一共要添加4次。

完成点击最上面一排Actions，再点kdts, 最后点击Run workflow测试邮箱是否收到邮件就OK了

我会持续更新 最近更新2022年12月9日
