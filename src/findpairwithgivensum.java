public class Main {
    /**
     * Approach:
     * We use hashMap, the hashMap'key is the one of part of the target sum.
     * And we also use largest variable to record largest number in the result.
     * We check each element of nums, if hashMap contains key of 'target - nums[i]',
     * then we find the one of possible result, and we also need to check is one of result is larger than largest,
     * if so, then we update result.
     *
     * Time Complexity : O(n) n is length of nums
     * Space Complexity : we use hashMap so the space complexity is O(n), n is length of nums
     */
    public static void main(String[] args) {
        int[] nums = new int[]{20, 50, 40, 25, 30, 10};
        int[] res = twoSum(nums, 90);
        String str = "[" + res[0] + "," + res[1] + "]";
        System.out.println(str);
    }

    private static int[] twoSum(int[] nums, int target){
        int[] res = new int[2];
        int largest = 0;
        target -= 30;
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int oneOfSum = target - nums[i];
            // find the other part of sum, and larger than largest
            if((oneOfSum > largest || nums[i] > largest)
                    && hashMap.containsKey(oneOfSum)){
                res[0] = hashMap.get(oneOfSum);
                res[1] = i;
                largest = Math.max(oneOfSum, nums[i]);
            }
            hashMap.put(nums[i], i);
        }
        return res;
    }
}