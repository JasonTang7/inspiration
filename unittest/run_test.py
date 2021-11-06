import re
from typing import SupportsBytes
import unittest
from unittest import runner
from utility.HTMLTestRunner import HTMLTestRunner
import time
import yagmail
import config

#把测试报告作为附件发送到指定邮箱
def send_mail(report):
    #发件邮箱
    yag = yagmail.SMTP(user="qa.cn@yamibuy.com",password="xayamibuy.com",host='smtp.gmail.com')
    subject = "自动化测试报告"
    contents = "自动化测试执行完毕，请查看附件中的测试报告。"
    #收件邮箱
    yag.send(config.to,subject,contents,report)
    print("邮件已发送！")

if __name__ == '__main__':
    #定义测试用例的目录为当前目录下的test_case目录
    test_dir = 'unittest/test_case/'
    suit = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    #取当前日期时间
    now_time = time.strftime("%Y%m%d%H%M%S")
    #生成HTML格式的报告
    html_report = 'unittest/test_report/' + now_time + 'result.html'
    fp = open(html_report,'wb')
    #调用HTMLRUNNER运行测试用例
    runner = HTMLTestRunner(stream=fp, title="YAMI测试报告", description="运行环境:Chrome浏览器" )
    runner.run(suit)
    fp.close()
    
    #发送报告
    send_mail(html_report)