class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self._permute_helper(nums, [])

    def _permute_helper(self, nums: list, values: list = []) -> list:
        if len(nums) == 0:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self._permute_helper(nums[:i] + nums[i + 1:], values + [nums[i]])
        return result

