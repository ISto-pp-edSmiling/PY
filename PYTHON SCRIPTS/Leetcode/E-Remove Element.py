class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
            nums[:]=[l for l in nums if l!=val]

# given an array remove all int == val.
            