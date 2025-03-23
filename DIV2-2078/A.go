package main

import "fmt"

func main() {

	var testcases int
	fmt.Scan(&testcases)

	inputs := make([][]int, testcases)

	for i := range testcases {
		// scan two lines
		var n, x int
		fmt.Scan(&n, &x)

		arr := make([]int, n)
		for j := range n {
			fmt.Scan(&arr[j])
		}

		testcases[i] = arr

	}

	for i := range testcases {
		fmt.Println(inputs[i])
	}

}
