package main

import (
	"fmt"
)

func numberOfDeletions(str1, str2 string) int {

	i := len(str1) - 1 // i for str1
	j := len(str2) - 1 // j for str2

	for i >= 0 && j >= 0 {
		// fmt.Println("check:", string(str1[i]), string(str2[j]))
		if str2[j] == str1[i] {
			//traversing back
			i--
			j--
		} else {
			break
		}

	}

	// fmt.Println(lenLongestCommonSuffix)
	return len(str1) + len(str2) - (2 * (len(str1) - 1 - i))

}

func main() {
	var str1, str2 string
	fmt.Scan(&str1)
	fmt.Scan(&str2)

	fmt.Print(numberOfDeletions(str1, str2))
}
