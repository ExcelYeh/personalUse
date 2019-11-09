'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def reverse(self, x: int) -> int:
       
        # 处理符号
        sign=0;
        if(x<0):
            sign=-1
            x=abs(x)
        #反转数字
        s=str(x)
        s=s[::-1]
        x = int(s)
        if(sign==-1):
            x *=(-1)
         # 是否在范围内
        if(abs(x)>=pow(2,31)):
            return 0
        elif(x==(pow(2,31)*(-1))):
            return 0
        return x
