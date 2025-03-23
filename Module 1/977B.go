package main

import "fmt"

func main() {
	n := 0
	fmt.Scan(&n)

	var str string
	fmt.Scan(&str)

	counts := make(map[string]int)

	for i := 1; i < len(str); i++ {
		temp := string(str[i-1]) + string(str[i])
		counts[temp] += 1
	}

	type MaxPair struct {
		maxKey   string
		maxValue int
	}

	var res MaxPair

	for k, v := range counts {
		if res.maxValue < v {
			res.maxKey = k
			res.maxValue = v
		}

	}

	fmt.Println(res.maxKey)

}
