
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive(nums):

    if len(nums) == 0:
        return None
    else:
        mid = len(nums) // 2
        return TreeNode(nums[mid], recursive(nums[:mid]), recursive(nums[mid + 1:]))

result = recursive([-10,-3,0,5,9])
print(result)