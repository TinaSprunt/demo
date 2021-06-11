# coding:utf-8
#生成网页测试结果的demo

"""
casePath = "D:\PycharmProjects\demo2\case"   #测试case的路径
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(casePath,pattern='test*.py',top_level_dir=None)#检索所有符合这个命名规则的文件
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="E:\\PythonTestData\\report\\"+now+"_result.html"  #规定结果文件存储路径和命名
fp=open(filename,'wb') #创建空的测试报告html文件

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())#运行测试容器中的用例，并将结果写入的报告中

#关闭文件流，不关的话生成的报告是空的
fp.close()"""

