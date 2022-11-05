class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        i = 0
        while i < (len(nums)-2):
            if len(result) > 0:
                if result[len(result)-1][0] == nums[i]:
                    i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[j] + nums[k]) > (0 - nums[i]):
                    k -= 1
                elif (nums[j] + nums[k]) < (0 - nums[i]):
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
            i += 1
        return result
# This 3 Sum question can be trans to [len(nums) - 2] 2 Sum questions.
# Attention:
# if you want to remove the duplicate list in the result,
# you cannot use "Set",
# because "Set" can not contain mutable objects. Lists are mutable.