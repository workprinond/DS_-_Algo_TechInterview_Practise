public class productsuggestion {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        if(products == null || products.length == 0 || searchWord == null || searchWord.isEmpty()){
            return new ArrayList<>();
        }
        // build trie
        TrieNode root = new TrieNode();
        for(String p : products){
            TrieNode cur = root;
            // insert current product into Trie.
            for(char c : p.toCharArray()){
                if(cur.children[c - 'a'] == null){
                    cur.children[c - 'a'] = new TrieNode();
                }
                cur = cur.children[c - 'a'];
                // put products with same prefix into suggestion list.
                cur.suggestion.offer(p);
                // sort products
                Collections.sort(cur.suggestion);
                // if exceed 3, poll last element
                if(cur.suggestion.size() > 3){
                    cur.suggestion.pollLast();
                }
            }
        }
        List<List<String>> res = new ArrayList<>();
        for(char c : searchWord.toCharArray()){
            if(root != null){
                root = root.children[c - 'a'];
            }
            res.add(root == null ? new ArrayList<>() : root.suggestion);
        }

        return res;
    }

    class TrieNode{
        TrieNode[] children;
        LinkedList<String> suggestion;

        public TrieNode(){
            children = new TrieNode[26];
            suggestion = new LinkedList<>();
        }
    }
}
