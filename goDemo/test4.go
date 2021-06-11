package main

import "fmt"

func main() {

	blance := [...]float32{12.55, 13, 14}

	//用range遍历拿到的只是数组的拷贝值，要修改数组内容得用下标
	for _, v := range blance {
		fmt.Println(v)
	}
}
