package main

import "fmt"

func main() {

	//指针
	var a int
	var ptr *int
	var xptr **int

	a = 10
	ptr = &a
	xptr = &ptr

	fmt.Println("a的指针 %d \n", *ptr)

	//指向指针的指针
	fmt.Println("指向a指针的指针 %d \n", **xptr)

	//指针数组
	b := []int{11, 12, 13}

	var i int
	var dataPtr [3]*int

	for i = 0; i < 3; i++ {
		dataPtr[i] = &b[i]
	}

	for i = 0; i < 3; i++ {
		fmt.Println("a[%d] = %d", i, *dataPtr[i])
	}

}
