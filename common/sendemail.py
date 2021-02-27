#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

from common.getconf import Config
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from common.getfiledir import REPORTDIR
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class OperEmail(object):
    def __init__(self):
        """
            获取文件路径及相关配置
        """
        self.conf = Config()
        # all_path = []
        self.filename = os.path.join(REPORTDIR,'reporter.html')

        self.host = self.conf.get('email','host')
        self.port = self.conf.get('email','port')
        self.user = self.conf.get('email','user')
        self.pwd = self.conf.get('email','pwd')
        self.from_addr = self.conf.get('email','from_addr')
        self.to_addr = self.conf.get('email','to_addr')

    def get_email_host_smtp(self):
        """
            连接smtp服务器
        """
        self.smtp = smtplib.SMTP_SSL(host=self.host,port=self.port)
        self.smtp.login(user=self.user,password=self.pwd)

    def made_msg(self):
        """
            构建一封邮件
        :return:
        """
        self.msg = MIMEMultipart()

        with open(self.filename,'r') as f:
            content = f.read()
        text_msg = MIMEText(content,_subtype='html',_charset='utf-8')   # 创建文本内容
        self.msg.attach(text_msg)   # 添加到多邮件的组件中
        # 创建邮件的附件
        report_file = MIMEApplication(content)
        report_file.add_header('Content-Disosition','attachment',filename=str.split(self.filename,'\\').pop())
        self.msg.attach(report_file)

        self.msg['subject'] = '自动化测试报告'
        self.msg['form'] = self.from_addr
        self.msg['to'] = self.to_addr

    def send_email(self):
        """
            发送邮件
        """
        self.get_email_host_smtp()
        self.made_msg()
        self.smtp.send_message(self.msg,from_addr=self.from_addr,to_addrs=self.to_addr)



