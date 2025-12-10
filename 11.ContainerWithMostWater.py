# inptput:一個List裡面裝柱體高度(不可重新排序)
# output:最大面積(string)



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            less_length=min(height[left],height[right])
            area=less_length*(right-left)
            max_area=max(max_area,area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_area