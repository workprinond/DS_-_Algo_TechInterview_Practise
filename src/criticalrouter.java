
    class Rextester
    {
        public static void main(String[] args) {
            int numRouters1 = 5;
            int numLinks1 = 6;
            int[][] links1 = {{0, 1}, {1, 2}, {0, 2}, {2, 3}, {2, 4}, {3, 4}};
            System.out.println(getCriticalNodes(links1, numLinks1, numRouters1));

            int numRouters2 = 5;
            int numLinks2 = 5;
            int[][] links2 = {{0, 1}, {1, 2}, {0, 2}, {0, 3}, {3, 4}};
            System.out.println(getCriticalNodes(links2, numLinks2, numRouters2));

            int numRouters3 = 4;
            int numLinks3 = 3;
            int[][] links3 = {{0, 1}, {1, 2}, {2, 3}};
            System.out.println(getCriticalNodes(links3, numLinks3, numRouters3));

            int numRouters4 = 7;
            int numLinks4 = 7;
            int[][] links4 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}};
            System.out.println(getCriticalNodes(links4, numLinks4, numRouters4));

            int numRouters5 = 4;
            int numLinks5 = 4;
            int[][] links5 = {{0, 1}, {0, 2}, {0, 3}};
            System.out.println(getCriticalNodes(links5, numLinks5, numRouters5));
        }

        static int time = 0;
        private static List<Integer> getCriticalNodes(int[][] links, int numLinks, int numRouters) {
            time = 0;
            Map<Integer, Set<Integer>> map = new HashMap<>();
            for(int i=0;i< numRouters;i++) {
                map.put(i, new HashSet<>());
            }
            for(int[] link : links) {
                map.get(link[0]).add(link[1]);
                map.get(link[1]).add(link[0]);
            }
            Set<Integer> set = new HashSet<>();
            int[] low = new int[numRouters];
            int[] disc = new int[numRouters];
            int parent[] = new int[numRouters];
            Arrays.fill(disc, -1);
            Arrays.fill(parent, -1);
            for(int i= 0; i< numRouters; i++) {
                if(disc[i] == -1)
                    dfs(map, low, disc, parent, i, set);
            }
            return new ArrayList<>(set);
        }



        private static void dfs(Map<Integer, Set<Integer>> map, int[] low, int[] disc, int[] parent, int u, Set<Integer> res) {
            int children = 0;
            disc[u] = low[u]= ++time;
            for(int v : map.get(u)) {
                // it mean not visited
                if(disc[v] == -1) {
                    children++;
                    // update v's parent is u
                    parent[v] = u;
                    // explore
                    dfs(map, low, disc, parent, v, res);
                    // Check if the subtree rooted with v has a connection to one of the ancestors of u
                    low[u] = Math.min(low[u], low[v]);
                    // if parent[u] == -1, it means is root, and if it has more than 1 children it cannot be removed
                    // whereas if u is not root and low value of one of its child is more than discovery value of u.
                    if((parent[u] == -1 && children > 1) || (parent[u] != -1 && low[v] >= disc[u]))
                        res.add(u);
                }
                else if(v != parent[u])
                    // Update low value of u for parent function calls.
                    low[u] = Math.min(low[u], disc[v]);
            }
        }
    }

