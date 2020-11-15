public class criticalrouters3import java.util.ArrayList;

// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        int[][] e = new int[][]{{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}};
        int v = 7;

        ArrayList<Integer> list = new ArrayList<>();

        for(int i=0; i<v; i++){
            //i is the edge I'm ignoring
            if(!helper(e, i, v)){
                list.add(i);
            }
        }

        System.out.println(list);
    }

    public static boolean helper(int[][] e, int v, int total){
        HashSet<Integer> set = new HashSet<>();
        boolean firstAdd = false;

        for(int i=0; i<e.length; i++){
            //ignores edges that have v as starting or ending point
            if(e[i][0] == v || e[i][1] == v)
                continue;

            //adding any edge as the starting point, both vertices
            //will fail if the edges are self edges
            if(!firstAdd){
                set.add(e[i][0]);
                set.add(e[i][1]);
                firstAdd = true;
            }

            //if the next edge has one of the edges already in the set, I can visit it
            if(set.contains(e[i][0]) || set.contains(e[i][1])){
                set.add(e[i][0]);
                set.add(e[i][1]);
            }
        }

        //if total visited elements equals all vertices - removed vertice
        return set.size() == total - 1;
    }

} {
}
