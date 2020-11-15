public class Main {
    /**
     * Apporach
     * Kruskal's Minimum Cost Spanning Tree Algorithm
     * v -> vertices, e -> edges
     * Time Complexity: O(vloge)
     * Space Complexity: O(v)
     *
     * Basiclly I use Kruskal’s algorithm to generate a minimum spanning tree for the graph.
     * Use Union-Find to see wether we can add an edge or not,
     * the condition to add an edge if it's not belong to existing connected component.
     * Idea is simple:
     * Sort new edges to no-descresing order
     * Pick the smallest edge from new edges
     * Repeat until MST is formed and every node is connected.
     **/
    private static int[] parent;
    public static void main(String[] args) {
        System.out.println("Hello World!");
        int tc1 = minCostRepairRoad(5, new int[][]{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 5}}, new int[][]{{1, 2, 12}, {3, 4, 30}, {1, 5, 8}});
        int tc2 = minCostRepairRoad(6, new int[][]{{1, 2}, {2, 3}, {4, 5}, {3, 5}, {1, 6}, {2, 4}}, new int[][]{{1, 6, 410}, {2, 4, 800}});
        int tc3 = minCostRepairRoad(6, new int[][]{{1, 2}, {2, 3}, {4, 5}, {5, 6}, {1, 5}, {2, 4}, {3, 4}}, new int[][]{{1, 5, 110}, {2, 4, 84}, {3, 4, 79}});

        System.out.println("res1: " + tc1);
        System.out.println("res2: " + tc2);
        System.out.println("res3: " + tc3);

    }

    private static int minCostRepairRoad(int n,
                                         int[][] edges,
                                         int[][] repairEdges){
        int connect = n;
        parent = new int[n + 1];
        HashSet<String> hashSet = new HashSet<>();

        // let each node's parent is itslef int the beginning
        for(int i = 0; i <= n; i++){
            parent[i] = i;
        }

        // add borken edge into hashSet, then we can detect broken edges
        for(int[] newEdge : repairEdges){
            StringBuilder sb = new StringBuilder();
            sb.append(newEdge[0]).append("#").append(newEdge[1]);
            hashSet.add(sb.toString());
        }

        for(int[] edge : edges){
            StringBuilder sb = new StringBuilder();
            sb.append(edge[0]).append("#").append(edge[1]);
            if(!hashSet.contains(sb.toString())){
                if(union(edge[0], edge[1])){
                    // union it, so connect minus 1
                    connect--;
                }
            }
        }

        // becasue we want to find min cost, we can sort repair array by their cost
        Arrays.sort(repairEdges,(a, b) -> a[2] - b[2]);

        int minCost = 0;
        for(int[] repairEdge : repairEdges){
            // can union it, minus 1
            if(union(repairEdge[0], repairEdge[1])){
                // add minCost
                minCost += repairEdge[2];
                connect--;

            }
            // if connect = 1, it means all node's is accessible
            if(connect == 1){
                return minCost;
            }
        }

        return connect == 1 ? minCost : -1;
    }

    private static boolean union(int x, int y){
        int setX = find(x);
        int setY = find(y);
        // it means they are not in the same group, union it
        if(setX != setY){
            parent[setY] = setX;
            return true;
        }
        // if they are in the same union, then we don't need to union
        return false;
    }

    private static int find(int x){
        // flat nodes and find it's parent's parents
        if(parent[x] != x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}