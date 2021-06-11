package main

import "fmt"

func main() {

	//map需要初始化，不初始化会创建出一个nil map ,nil map 无法用来存放键值对
	var provinceMap map[string]string
	provinceMap = make(map[string]string)

	provinceMap["shanxi"] = "xian"
	provinceMap["shanghai"] = "shanghai"
	provinceMap["hainan"] = "haikou"

	//遍历map
	for city := range provinceMap {
		fmt.Println(city, " city is ", provinceMap[city])
	}

	//删除元素
	delete(provinceMap, "hainan")

	//查询某个值是否存在于map中
	cityName, isok := provinceMap["hainan"]

	if isok {
		fmt.Println(cityName, "ok")
	} else {
		fmt.Println("wrong")
	}

}
