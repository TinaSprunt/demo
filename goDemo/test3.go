package main

import "fmt"

type cb func(int) int

func main() {
	testCallBack(1, callBack)
	testCallBack(2, func(x int) int {
		fmt.Println("直接写在参数里的回调")
		return x
	})

}

func testCallBack(x int, f cb) {
	//形参是什么这里就是什么
	f(x)
}

func callBack(x int) int {
	fmt.Println("抽成函数的回调，以函数做参数")
	return x
}
