class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        for i in range(0, l):
            for b in range(0, l):
                if nums[i] + nums[b] == target and i != b:
                    return([i, b])