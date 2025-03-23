package main

import (
	"fmt"
	s "strings"
)

func convertToNormal(str string) string {
	//check if capslock string
	if s.ToLower(string(str[0])) == string(str[0]) && s.ToUpper(str[1:]) == str[1:] {
		return s.ToUpper(str[:1]) + s.ToLower(str[1:])
	} else if s.ToUpper(str[0:]) == str[0:] {
		return s.ToLower(str)
	} else {
		return str
	}

}

func main() {

	var str string

	fmt.Scan(&str)
	fmt.Println(convertToNormal(str))

}
