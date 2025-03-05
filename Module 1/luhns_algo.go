package main

import (
	"fmt"
)

func addTheDigits(num int) int {
	sum := 0
	for num != 0 {
		sum = sum + (num % 10)
		num = num / 10
	}
	return sum
}

func lunhsAlgoSum(length int, nums []int) int {
	res_sum := 0

	for i := range length {
		res := 0
		if i%2 == 0 {
			// double if second digit
			d := 2 * nums[i]
			if d%10 == d {
				// result is a single digit so keep it
				res = d
			} else {
				//if a double digit, then add the digits
				res = addTheDigits(d)
			}
		} else {
			res = nums[i]
		}
		// fmt.Print(res, " ")
		res_sum = res_sum + res
	}
	return res_sum
}

func isAValidCreditCard(length int, nums []int) bool {
	algoSum := lunhsAlgoSum(length, nums)
	if algoSum%10 == 0 {
		return true
	} else {
		return false
	}
}

func main() {

	const length = 16

	nums := make([]int, length)

	for i := range length {
		fmt.Scan(&nums[i])
	}

	fmt.Print(isAValidCreditCard(length, nums))

}
