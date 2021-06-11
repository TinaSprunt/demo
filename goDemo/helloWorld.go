package main

import "fmt"

func testFun(year string) (string string) {

	var res string = year + "-03-04"
	var msg2 string = "hello "
	return res, msg2
}

func main() {

	var stockcode = 123
	var msg = "2021-3-4"
	var url = "code=%d&enDate=%s"
	var target = fmt.Sprintf(url, stockcode, msg)

	fmt.Println(target)

	//可以只定义变量不赋值，这样会输出对应变量类型的0值，比如string就是 ""
	var i int
	var f float64
	var b bool
	var s string

	fmt.Println("%v %v %v %q\n", i, f, b, s)

	//全局变量是允许声明但不使用的,其他变量声明后必须使用

	res, msg2 = testFun("2020")
	fmt.Println(res, msg2)

}
