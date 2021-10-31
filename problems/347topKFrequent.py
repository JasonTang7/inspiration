"""给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freList = self.freqList(nums)
        answer = []
        for i in range(k):
            answer.append(freList[i])
        return answer
    
    def freqList(self,nums:List[int])->List[int]:
        #返回按nums中频率从高到低排序的不重复整数列表
        """
        1、用一个列表存nums中每个元素的出现次数
        2、按出现次序倒序排列存入另一个列表
        3、按第二个列表的顺序找第一个列表的索引（只找不重复的数）
        4、根据找到的索引找到nums中对应的元素，添加到一个列表中，并返回
        """
        times = []
        freList = []
        difftimes=[]
        catch = []
        for i in range(len(nums)):
            a=0 #计算每一个元素出现次数
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    a = a+1
            times.append(a)
        revtimes = times
        for i in range(len(revtimes)):
            if nums[i] not in catch:
                catch.append(nums[i])
                difftimes.append(revtimes[i])
        difftimes.sort(reverse=True)
        for i in range(len(difftimes)):
            for j in range(len(times)):
                if difftimes[i] == times[j]:
                    if nums[j] not in freList:
                        freList.append(nums[j])
        return freList

sol = Solution()
nums = [1,2]
k =2
answer = sol.topKFrequent(nums,k)
print(answer)