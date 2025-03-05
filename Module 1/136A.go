package main

import (
	"fmt"
	"slices"
)

/**
Friend No. 1 2 3 4
		Pi 2 3 4 1

*/

func main() {
	var n int
	fmt.Scan(&n)

	var nums = make([]int, n)

	for i := range n {
		fmt.Scan(&nums[i])
	}

	for i := range n {
		fmt.Print(slices.Index(nums, i+1) + 1)
		if i < n-1 {
			fmt.Print(" ")
		}
	}

}
