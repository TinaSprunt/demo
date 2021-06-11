package main

import "fmt"

type People struct {
	name   string
	age    int
	gender string
}

func main() {

	var woman People
	var man People

	woman.name = "nuna"
	woman.age = 23
	woman.gender = "famale"

	man.name = "jeo"
	man.age = 27
	man.gender = "male"

	printPeople(&woman)
	printPeople(&man)

}

func printPeople(people *People) {
	fmt.Println(people.name)
	fmt.Println(people.age)
	fmt.Println(people.gender)
}
