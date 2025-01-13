package main

import "fmt"

func intSum() func() int {
	i := 10
	return func() int {
		i *= 2
		return i
	}
}

func main() {
	nextInt := intSum()

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	newInts := intSum()
	fmt.Println(newInts())
}