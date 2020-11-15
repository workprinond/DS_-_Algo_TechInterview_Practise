public class mincostconnectsticks {
    public int connectSticks(int[] sticks) {
        if(sticks == null || sticks.length == 0){
            return 0;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a - b);

        for(int stick : sticks){
            pq.offer(stick);
        }

        int res = 0;
        while(pq.size() > 1){
            int n1 = pq.poll();
            int n2 = pq.poll();
            int sum = n1 + n2;
            res += sum;
            pq.offer(sum);
        }

        return res;
    }
}
