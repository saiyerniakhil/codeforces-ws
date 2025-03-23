package main

import "fmt"

func decode(str string) {
	strLen := len(str)
	res := []string{}
	for i := strLen - 1; i >= 0; i-- {
		currLen := strLen - i
		idx := currLen / 2
		res = append(res[:idx], append([]string{string(str[i])}, res[idx:]...)...)
	}

	for i := len(res) - 1; i >= 0; i-- {
		fmt.Print(res[i])
	}
}

func main() {
	var n int
	fmt.Scan(&n)
	var str string
	fmt.Scan(&str)

	decode(str)
}
