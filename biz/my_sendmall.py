#-*-coding:UTF-8-*-
#SMTP电子邮件发送
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr,formataddr
#先定义署名格式化函数
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#发送人，接收人
sender='357072695@qq.com'
pwd='eqaykvvzbsoebjdc' #请自行登陆邮箱打开SMTP服务，会自动生成第三方授权码，不是登陆密码！
# receiver='xuchen@bicai365.com'
receiver='357072695@qq.com'

# 格式化的署名和接收人信息
message = MIMEMultipart()
# message['From'] = _format_addr('这是xx<%s>'%sender)
message['From'] = _format_addr(sender)
message['To'] = _format_addr(receiver)
message['Subject'] = ('BICAI_GUI_FOR_ANDROID_REPORT')
message.attach(MIMEText('<html><body>'
                        +'<h1>比财安卓UI自动化报告</h1>'
                        +'<p>请注意查收附件'
                        +'</body></html>', 'html', 'utf-8'))

#MIMEImage，只要打开相应图片，再用read()方法读入数据，指明src中的代号是多少，如这里是'Imgid’，在HTML格式里就对应输入。
        # 增加附件1

dir_list = os.listdir(r'../report')
dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(r'/Users/xuchen/PycharmProjects/BCGTFA/report', x)))
att1 = MIMEText(open(r'../report/' + dir_list[-1], 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="bc_gui_andorid.html"'
message.attach(att1)

#发送邮件！
try:
    smtpobj=smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpobj.login(sender, pwd)
    smtpobj.sendmail(sender, [receiver], message.as_string())
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，Case:%s'%e)