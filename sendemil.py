from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
from email.mime.image import MIMEImage
def send(TET):
    mail_host = "smtp.163.com" #SMTP服务器地址
    mail_sender = "micaiabc@163.com" #账号
    mail_passwd = "OLDOJFMMIZDIEQFE" #密码

    msg = MIMEMultipart('related')
    msg["Subject"] = "快递"
    msg["From"] = mail_sender #发送人
    msg["To"] = "2544624953@qq.com" #接收人

    msgtet = MIMEText(TET + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), 'plain', 'utf-8')
    msg.attach(msgtet)
    ## 发送邮件
    s = smtplib.SMTP() #实例化对象
    s.connect(mail_host, 25) #连接163邮箱服务器，端口号为25
    s.login(mail_sender, mail_passwd) #登录邮箱
    s.sendmail(mail_sender, [msg["To"]], msg.as_string())
    s.quit()




