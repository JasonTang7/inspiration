"""给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums),1):
            for j in range(i+1,len(nums),1):
                if nums[i] + nums[j] == target:
                    list = []
                    list.append(i)
                    list.append(j)
                    return list


sol = Solution()
answer = sol.twoSum([2,7,11,15],9)
print(answer)