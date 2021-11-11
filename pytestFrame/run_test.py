# coding=utf-8
import os
import pytest
import click
import logging
import time
from config import RunConfig,StaticConfig
from conftest import REPORT_DIR
import yagmail

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''

def init_env(new_report):
    """初始化测试报告目录"""
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")
    

def send_mail(report):
    """把测试报告作为附件发送到指定邮箱"""
    #发件邮箱
    yag = yagmail.SMTP(user="qa.cn@yamibuy.com",password="xa@yamibuy.com",host='smtp.gmail.com')
    subject = "自动化测试报告"
    contents = "自动化测试执行完毕，请查看附件中的测试报告。"
    #收件邮箱
    yag.send(StaticConfig.email_cc,subject,contents,report)
    logger.info("邮件已发送！") 

@click.command()
@click.option('-m',default=None,help="输入运行模式：run 或 debug。")
#使用命令行工具库click，就不能直接在IDE中调试
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        RunConfig.NEW_REPORT = os.path.join(REPORT_DIR,now_time)
        init_env(RunConfig.NEW_REPORT)
        html_report = os.path.join(RunConfig.NEW_REPORT,"report.html")
        xml_report = os.path.join(RunConfig.NEW_REPORT,"junit-xml.xml")
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        logger.info("运行结束，生成测试报告！")
        send_mail(html_report)
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-s", "-v", RunConfig.cases_path])
        print("运行结束！！")

if __name__ == '__main__':
    #m = None
    run()       