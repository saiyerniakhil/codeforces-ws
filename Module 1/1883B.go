package main

import "fmt"

/*
Rules of a palindrome
- Incase of an 'even' lengthed string, it needs to have exactly equal number of letters
- Incase of an 'odd' lengthed string, the needs to have only one letter repeating odd number of times.

ababab - not a palindrome since 3 a's and 3 b's baaabb -> delete one char (a/b) -> baaab / abbba
abab - 2 a's 3 b's -> baab
*/
func processString(n int, k int, str string) string {

	charCounts := make(map[rune]int)
	for _, r := range str {
		charCounts[r]++
	}
	lettersWithOddFreq := 0
	lettersWithEvenFreq := 0

	for _, value := range charCounts {
		if value%2 == 0 {
			lettersWithEvenFreq += 1
		} else if value%2 == 1 {
			lettersWithOddFreq += 1
		}
	}

	if k == 0 {
		if lettersWithOddFreq > 1 {
			return "NO"
		}
	}

	minus := k
	for minus > 0 {
		if lettersWithOddFreq > 0 {
			lettersWithOddFreq -= 1
			lettersWithEvenFreq += 1
		} else {
			lettersWithEvenFreq -= 1
			lettersWithOddFreq += 1
		}
		minus -= 1
	}

	if lettersWithOddFreq > 1 {
		// fmt.Println(lettersWithEvenFreq, lettersWithOddFreq)
		return "NO"
	} else if lettersWithOddFreq == 0 {
		return "YES"
	}

	if lettersWithEvenFreq >= 1 {
		return "YES"
	} else {
		return "YES"
	}

}

func main() {
	n_test := 0
	fmt.Scan(&n_test)

	i := 0
	inputs := make([]string, n_test)
	for i < n_test {
		n, k := 0, 0
		var s string
		fmt.Scan(&n, &k)
		fmt.Scan(&s)
		inputs[i] = processString(n, k, s)
		i++
	}

	for i := range n_test {
		fmt.Println(inputs[i])
	}
}
