public class Main {
    // https://leetcode.com/discuss/interview-question/373202
    // aka. Foreground and Background
    /*
    Approach:
    We consider all of the combination to find the one with optimal value.
    Time complexity: We consider all of the combinations, so the time complexity is O(M*N)
    Space complexity: We use a variable to track the maximal value, the space complexity is O(1)
    */
    public static void main(String args[]){
        List<int[]> a1 = new ArrayList<>();
        a1.add(new int[]{1, 3});
        a1.add(new int[]{2, 5});
        a1.add(new int[]{3, 7});
        a1.add(new int[]{4, 10});
        List<int[]> b1 = new ArrayList<>();
        b1.add(new int[]{1, 5});
        b1.add(new int[]{2, 4});
        b1.add(new int[]{3, 1});
        b1.add(new int[]{4, 2});
        int	target = 10;
        for(int[] ele : getPairs(a1, b1, target)) {
            System.out.println(Arrays.toString(ele));
        }
    }

    private static List<int[]> getPairs(List<int[]> a1,
                                        List<int[]> b1,
                                        int target){
        // Collections.sort(a1, (n1, n2) -> n1[1] - n2[1]);
        // Collections.sort(b1, (n1, n2) -> n1[1] - n2[1]);
        List<int[]> res = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for(int[] a : a1){
            for(int[] b : b1){
                int sum = a[1] + b[1];
                if(sum > target || sum < max){
                    continue;
                }
                if(sum > max){
                    max = sum;
                    res.clear();
                }
                res.add(new int[]{a[0], b[0]});
            }
        }
        return res;
    }
}