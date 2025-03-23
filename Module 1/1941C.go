package main

import (
	"fmt"
)

func makeBeautiful(t int, str string) int {
	// collect the counts of each and every letter

	count := 0
	i := 0
	for i < t {
		if i+5 < t && string(str[i]) == "m" && string(str[i+1]) == "a" && string(str[i+2]) == "p" && string(str[i+3]) == "i" && string(str[i+4]) == "e" {
			count += 1
			i = i + 4
		} else if i+2 < t && string(str[i]) == "m" && string(str[i+1]) == "a" && string(str[i+2]) == "p" {
			count += 1
			i = i + 2
		} else if i+2 < t && string(str[i]) == "p" && string(str[i+1]) == "i" && string(str[i+2]) == "e" {
			count += 1
			i = i + 2
		}
		i += 1
	}

	return count

}

func main() {
	var n_test int
	fmt.Scan(&n_test)

	outputs := make([]int, n_test)

	for i := range n_test {
		var t int
		var test_i string
		fmt.Scan(&t)
		fmt.Scan(&test_i)
		outputs[i] = makeBeautiful(t, test_i)
	}

	for i := range n_test {
		if i == n_test-1 {
			fmt.Println(outputs[i])
		} else {
			fmt.Println(outputs[i])
		}
	}

}
