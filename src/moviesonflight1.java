public class Main {
    /**
     * Approach :
     * First we sort nums array, in order to use two pointer way.
     * We also need one max variable to record max sum of two movies.
     * We use two pointer way to find the sum of two movies.
     *
     * Time complexity : O(nlogn) because we sort nums, the time complexity is O(nlogn) the n is nums length
     * Space complexity : O(1) we just use one variable for max sum
     *
     */
    public static void main(String[] args) {
        System.out.println("Hello World!");
        int d = 250;
        int [] nums =  new int [] {90, 85, 75, 60, 120, 150, 125};
        int[] res = getTwoClosetSum(nums, d);
        System.out.println("res:" + res[0] + "," + res[1]);

    }

    private static int[] getTwoClosetSum(int [] nums, int d){
        Arrays.sort(nums);

        int i = 0;
        int j = nums.length - 1;
        int max = Integer.MIN_VALUE;
        d = d - 30;

        int[] res = new int[2];
        int start = 0;
        int end = 0;

        while(i < j){
            int sum = nums[i] + nums[j];
            if(sum <= d){
                if(sum > max){
                    max = sum;
                    res[0] = nums[i];
                    res[1] = nums[j];
                }
                i++;
            }else{
                j--;
            }
        }

        return res;
    }
}