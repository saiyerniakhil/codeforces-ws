package main

import "fmt"

func main() {
	var n, h int
	fmt.Scan(&n, &h)

	nums := make([]int, n) // declare a slice
	for i := range n {
		fmt.Scan(&nums[i])
	}

	sum := 0

	for i := range n {
		if nums[i] > h {
			sum = sum + 2
		} else if nums[i] <= h {
			sum = sum + 1
		}
	}

	fmt.Print(sum)

}
