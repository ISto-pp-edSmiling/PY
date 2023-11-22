# list.remove() removes all instances of a char in a list
# Leetcode question 283. Move Zeroes can be solved like this:
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

#but also like this:

class Solution:
    def moveZeroes(self, nums: list) -> None:
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
