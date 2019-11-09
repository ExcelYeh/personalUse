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
