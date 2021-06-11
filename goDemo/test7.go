package main

import "fmt"

func main() {

	//动态数组，也称之为切片，长度不固定，可以扩充
	s := []int{13, 14, 15}
	fmt.Println(len(s))

	//空切片
	var data []int

	fmt.Println(data)

	//切片追加元素，可以一个可以多个
	data = append(data, 16, 17, 19, 20, 21, 22)
	fmt.Println(data)

	//创建新切片,len计算长度，cap计算容量
	data2 := make([]int, len(data), (cap(data))*2)
	fmt.Println(cap(data2))

	//拷贝切片,拷贝data到data2
	copy(data2, data)
	fmt.Println(data2)

}
