class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        water_amount = 0
        while i<j :
            current_amount = min(height[i], height[j]) * (j-i)
            water_amount = max(water_amount, current_amount)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return water_amount

# 存水量是由宽度和最小高度决定的，一开始让宽度最宽。
# 如果想缩小宽度的同时增加高度，就要把最小的高度替换成它旁边的高度，才有可能增加最小高度
# 我一开始比较疑惑的问题是如果在中间有第一高和第二高板子呢
# 但后来想了一下，由于存水量由最小高度决定，除非最后同时走到这两个板子，他们的高度才会真的起作用，
# 这个指针算法可以保证最后能同时走到这两个板子