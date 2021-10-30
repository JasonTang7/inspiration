"""
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

 

示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
 

提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        cs =[]
        a=""
        for i in range(len(s)):
            cs.append(s[i])
        cs = self.reverseVowelsList(cs)
        return a.join(cs)
    
    def reverseVowelsList(self,cs:List) -> List:
        check = set(['a','e','i','o','u','A','E','I','O','U'])
        j = len(cs)-1
        for i in range(len(cs)):
            if cs[i] in check:
                while i < j:
                    if cs[j] in check:
                        a = cs [i]
                        cs[i] = cs[j]
                        cs[j] = a
                        j =j-1
                        break
                    else:
                        j = j -1
        return cs
