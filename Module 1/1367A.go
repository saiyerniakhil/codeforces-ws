package main

import "fmt"

func decodeString(str string) string {
	// abbaac
	/*
		start = 'a'
		step = 2
		ab
	*/
	start := str[0]
	var res string = string(start)

	if len(str) == 2 {
		return str
	}

	// fmt.Println(string(start))
	for i := 0; i < len(str); i += 2 {

		// fmt.Println("->", string(str[i]), " ", string(str[i+1]))
		if start == str[i] {
			res += string(str[i+1])
			start = str[i+1]
		}
	}
	return res
}

func main() {
	var n int
	fmt.Scan(&n)

	inputs := make([]string, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&inputs[i])
	}

	// fmt.Println("res===>")
	for i := 0; i < n; i++ {
		fmt.Println(decodeString(inputs[i]))
	}
}
