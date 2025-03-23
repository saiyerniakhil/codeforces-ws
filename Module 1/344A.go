package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	magnets := make([]int, n)

	for i := range n {
		fmt.Scan(&magnets[i])
	}

	count := 1 // we'll start with one group

	for i := range n - 1 {
		if magnets[i] != magnets[i+1] {
			count += 1
		}
	}

	fmt.Print(count)

}
