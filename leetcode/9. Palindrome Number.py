'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def getbit(self,x:int, index:int):
        # 索引： 个位为0，依次类推
        temp=x % pow(10,index+1) #取出从个位到index位的部分,位数为（index-1）位
        print(temp)
        temp /= pow(10,index)       #取出最高位数字
        return temp
        
    def isPalindrome(self, x: int) -> bool:
        #return(str(x)==str(x)[::-1])
        # 第一步判断是否为负数
        if(x<0):
            return False
        i=x
        count=0
        while(i>0):
            i/=10
            count+=1
        for j in range (count//2):
             # 索引： 个位为0，依次类推
            temp=x % pow(10,j+1) #取出从个位到index位的部分,位数为（index-1）位
            temp /= pow(10,j)       #取出最高位数字
            
             # 索引： 个位为0，依次类推
            temps=x % pow(10,count-j+1) #取出从个位到index位的部分,位数为（index-1）位
            temps /= pow(10,count-j)       #取出最高位数字
            if(temp!=temps):
                print(j)
                return False
        return True
