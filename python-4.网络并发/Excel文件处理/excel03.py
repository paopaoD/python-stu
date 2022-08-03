
'''
    用python发邮件
        SMTP(Simple Mail Transfer Protocol):即简单邮件传输协议

    python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件，
            它对smtp协议进行了简单的封装

'''
import smtplib
from email.mime.text import MIMEText    # 邮件正文
from email.header import Header     # 邮件头 (收件人信息)

#
# smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com",456)
# smtp_obj.login("252732030@qq.com","wangqi521124")




























