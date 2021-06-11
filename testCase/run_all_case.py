#在这个脚本里面去控制执行所有用例


#cod-ing utf-8
import unittest
import os



def allcase():
    case_path = "D:\PycharmProjects\demo2\case" #测试case的路径
    # case_path=os.path.join(os.getcwd(),"case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)#检索所有符合这个命名规则的文件

    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            testcase.addTest(test_case)
    return testcase


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(allcase())
















