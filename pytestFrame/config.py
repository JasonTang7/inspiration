import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))

class RunConfig():
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_case")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None

class StaticConfig():
    """静态配置"""
    pchome_url = "https://www.yamibuy.com"
    email_to =['jason.tang@yamibuy.com','812227984@qq.com']