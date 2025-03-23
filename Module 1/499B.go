package main

import (
	"fmt"
	"strings"
)

func translate(longToShortMap map[string]string, words []string) string {
	var res []string
	// words := strings.Split(strings.Replace(sentence, "\n", "", -1), " ")
	// fmt.Println(words)
	for idx := range words {
		if longToShortMap[words[idx]] != "" {
			// fmt.Println("found in map", idx, words[idx], longToShortMap[words[idx]])
			res = append(res, longToShortMap[words[idx]])
		} else {
			// fmt.Println("!found in map", idx, words[idx], longToShortMap[words[idx]])
			res = append(res, words[idx])
		}
	}
	// fmt.Println(longToShortMap)
	return strings.Join(res, " ")
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	longToShortMap := make(map[string]string)

	var i int
	for i < m {
		var word1, word2 string
		fmt.Scan(&word1, &word2)
		if len(word1) <= len(word2) {
			longToShortMap[word2] = word1
		} else {
			longToShortMap[word1] = word2
		}
		i += 1
	}

	// fmt.Println(longToShortMap)
	var sent []string
	var j int
	for j < n {
		var word string
		fmt.Scan(&word)
		sent = append(sent, word)
		j += 1
	}

	fmt.Println(translate(longToShortMap, sent))

}
