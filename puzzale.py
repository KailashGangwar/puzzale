# question
# Given an array, return a new array such that each element at index i of the new array
# is the product of all the numbers except the one at i [duplicate]

# arr[] of size n
# def productArray(arr, n):
# 	# Base case
# 	if(n == 1):
# 		print(0)
# 		return
# 	# Allocate memory for temporary arrays left[] and right[]
# 	left = [0]*n
# 	right = [0]*n
# 	# Allocate memory for the product array
# 	prod = [0]*n
# 	# Left most element of left array is always 1
# 	left[0] = 1
# 	# Right most element of right array is always 1
# 	right[n - 1] = 1
#     # print(right)
# 	# Construct the left array
# 	for i in range(1, n):
# 		left[i] = arr[i - 1] * left[i - 1]
# 	# Construct the right array
# 	for j in range(n-2, -1, -1):
#     	# print(j)
# 		right[j] = arr[j + 1] * right[j + 1]
# 	# Construct the product array using
# 	# left[] and right[]
# 	for i in range(n):
# 		prod[i] = left[i] * right[i]
# 	# print the constructed prod array
# 	for i in range(n):
# 		print(prod[i], end=' ')
# # Driver code
# arr = [3,2,1]
# n = len(arr)
# print("The product array is:")
# productArray(arr, n)


# (2nd soluation)
# Python program for product array puzzle
# with O(n) time and O(1) space.
# def solve(arr, n):
# 	prod = 1
# 	for i in arr:
# 		prod *= i
# 	# we know x / y mathematically is same
# 	# as x*(y to power -1)
# 	for i in arr:
# 		print(int(prod*(i**-1)), end =" ")
# # Driver Code
# arr = [3,2,1]
# n = len(arr)
# solve(arr, n)


# <-------------------------------------------------------------------->
# question 1st solutaion
# given an array of integers, find the first missing positive integer in linear time and constant space.
# in other words find and constant space. in other words
def firstMissingPositive(nums):

    for i in range(len(nums)):
        while 0 <= nums[i] - 1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i] - 1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
# nums = [1,2,0]
# print(firstMissingPositive(nums))

# question 2nd solutaion
# given an array of integers, find the first missing positive integer in linear time and constant space.
# in other words find and constant space. in other words
def firstMissingPositive(nums):
    n = 1
    s = set(nums)
    while n in s:
        n += 1
    return n
nums = [1,2,0]
print(firstMissingPositive(nums))
