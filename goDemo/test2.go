package main

import "fmt"

func main() {
	a, b := testFun("2020")
	fmt.Println(a, b)
}

func testFun(year string) (string, string) {
	res := year + "-03-04"
	msg := "hello"
	return res, msg
}

// go 函数可以返回多个值
// :=是声明以及赋值语句，对于已经声明过的变量不能用
