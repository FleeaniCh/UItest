import os

projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # 项目文件夹路径
# print(projectDir)  # D:\self-Study\code\testUI

CONFDIR = os.path.join(projectDir, 'conf')  # 配置文件路径
print(CONFDIR)

BASEFACTORYDIR = r'C:\Python\Python39\\'

DATADIR = os.path.join(projectDir,'data')
# print(DATADIR)

RESULTDIR = os.path.join(projectDir, 'result')  # D:\self-Study\code\testUI\result

SCREENSHOTDIR = os.path.join(RESULTDIR, 'screenshot')   # 截图文件路径
# print(RESULTDIR)

LOGDIR = os.path.join(RESULTDIR,'log')  # 日志文件路径

REPORTDIR = os.path.join(RESULTDIR,'report')    # 报告文件路径

CASEDIR = os.path.join(projectDir,'executetest')    # 测试用例文件夹
# print(CASEDIR)

