from typing import List


## Question 152. Maximum Product Subarray
"""
[-4,-3,-2]
max, min, prod = 
-4, -4, -4
12, -3, 12
6, -2, 12

"""


class MaxProductSolution:

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        max_product = nums[0]
        min_product = nums[0]
        final_max = nums[0]
        for num in nums[1:]:
            temp = max(num, num*max_product, min_product*num)
            min_product = min(num, num*min_product, max_product*num)
            max_product = temp
            final_max = max(max_product, final_max, min_product)
        return final_max

# attempts = 1

"""
1,1,1,0,0,0,1,1,1,1,0, K = 2
ptr1, ptr2, count0
if count0 == k:
    max_1s = max(max_1s, cur_1s)
elif count0 > k:
    ptr1=ptr2 

"""


# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         ptr1 = 0
#         ptr2 = 0
#         max1s = 0
#         count0 = 0
#         for index, num in enumerate(A):
#             ptr2 = index
#             if num == 0:
#                 if count0 == K:
#                     max1s = max(max1s, ptr2-ptr1)
#                 else:
#                     max1s = max(max1s, ptr2-ptr1+1)
#                 count0 += 1
#             else:
#                 max1s = max(max1s, ptr2-ptr1+1)
#             if count0 > K:
#                 while A[ptr1] != 0:
#                     ptr1 += 1
#                 ptr1 += 1
#                 count0 -= 1
#         return max1s

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1
        return right - left + 1