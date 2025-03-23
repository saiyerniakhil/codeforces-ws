package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	i := 0
	max := 0
	sum := 0

	for i < n {
		var enter, exit int
		fmt.Scan(&exit, &enter)
		temp := sum - exit + enter // max capacity at a given time

		// fmt.Println("=============")

		sum = temp
		// fmt.Println(">>>>", exit, enter, sum, max)
		// fmt.Println("=============")
		if max < temp {
			max = temp
		}
		i += 1
	}

	fmt.Println(max)

}
