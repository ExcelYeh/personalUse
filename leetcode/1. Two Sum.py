'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*********************************/
        // 暴力算解
        int[] index={0, 0};
        boolean sign = false;
        for(int i = 0; i<nums.length&& (!sign); i++){
            for(int j=i+1; j<nums.length&&(!sign); j++){
                if(target == (nums[i]+nums[j])){
                    index[0]=i;
                    index[1]=j;
                    sign = true;
                }
            }
        }
        return index;
    }
}
