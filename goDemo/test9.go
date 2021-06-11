package main

import "fmt"

//递归

func main() {

	var i int
	i = 3
	fmt.Printf("输入是 %d 输出是 %d\n", i, res(i))
}

func res(n int) int {

	n++
	fmt.Printf("%d", n)

	if n < 30 {
		return res(n)
	}

	return n

}
