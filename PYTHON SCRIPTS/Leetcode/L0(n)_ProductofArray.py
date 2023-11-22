class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = 1
        list=[]
        for num in nums:
            for n in nums[nums.index(num)+1:]:
                k *= n
            if not nums[:nums.index(num)] == []:
                for n in nums[:nums.index(num)]:
                    k *= n
            list.append(k)
            k = 1            
        return list       

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]