'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution {
    public int shortestSubarray(int[] A, int K) {
        // 最短子数组
        
        for (int len=0;len<A.length;len++){//偏移量
            for(int begin=0;begin<A.length-len;begin++){// 第一位元素的位置
                int sum = 0;
                for(int i=begin;i<=len+begin;i++){// 取出偏置范围内所有元素
                    sum += A[i];                // 算出总和
                }
                if(sum>=K){     // 如果子串和不小于K 返回长度
                    return len+1;
                }
            }
        }
        return -1;
    }
}
