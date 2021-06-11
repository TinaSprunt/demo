# demo

各种demo练习

## 1. goDemo go语法学习
## 2. testCase 简单的测试用例
## 3. pressureTest 压力测试
queue队列实现多线程压力测试（有待完善）

主线程完成数据准备，子线程进行IO操作，登录注册删除等数据准备、返回值校验，数据计算都不要放在子线程，只有网络请求放在子线程。用全局queue队列完成数据传递， queue队列自带线程互斥锁，队列为空自动阻塞

prepare_queue压测数据准备，填充队列queue

prepare_login模拟登录，更新headers

createThread创建子线程，并在子线程中调用包含IO操作的函数












































