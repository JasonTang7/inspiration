"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:
输入: s = ""
输出: 0
 
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        if not len(s):
            return n
        for i in range(0,len(s),1):
            for j in range(i+1,len(s),1):
                if s[i] == s[j]:
                    if j -i > 2:
                        for k in range(i+1,j,1):
                            for l in range(k+1,j,1):
                                if s[k] == s[l]:
                                    if k - i +1 > n:
                                        n = k - i +1
                                        break
                                else:
                                    if l - i + 1> n:
                                        n = l- i +1 
                                        continue 
                            break
                        break
                    elif j - i == 2:
                        n = 2
                        break
                    else:
                        n = 1
                        break
                else:
                    if j -i > 1:
                        for k in range(i+1,j,1):
                            for l in range(k+1,j+1,1):
                                if s[k] == s[l]:
                                    if k - i + 1> n:
                                        n = k - i +1
                                        break
                                else:
                                    if l - i +1> n:
                                        n = l- i +1
                                        continue
                            break
                        
                    else:
                        continue

        return n

sol = Solution()
answer = sol.lengthOfLongestSubstring("abcabcbb")
print(answer)




