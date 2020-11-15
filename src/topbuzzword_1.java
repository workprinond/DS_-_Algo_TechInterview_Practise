public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        String[] toys = new String[]{"elmo", "elsa", "legos", "drone", "tablet", "warcraft"};
        String[] quotes = new String[]{
                "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
                "The new Elmo dolls are super high quality",
                "Expect the Elsa dolls to be very popular this year, Elsa!",
                "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
                "For parents of older kids, look into buying them a drone",
                "Warcraft is slowly rising in popularity ahead of the holiday season"};
        List<String> res = topBuzzWord(6, 2, toys, 6, quotes);
        System.out.println(res);
    }

    public static List<String> topBuzzWord(int numToys, int topToys, String[] toys, int numQuotes, String[] quotes) {
        if(numToys == 0 || topToys == 0){
            return new ArrayList<>();
        }
        HashMap<String, WordStats> hashMap = new HashMap<>();
        for(String toy : toys){
            hashMap.put(toy, new WordStats(toy, 0));
        }
        for(int i = 0; i < quotes.length; i++){
            String quote = quotes[i].replaceAll("[\\!?,;.]", "").toLowerCase();
            String[] words = quote.split(" ");
            for(String w : words){
                if(hashMap.containsKey(w)){
                    WordStats ws = hashMap.get(w);
                    ws.frequency++;
                    ws.quotesIds.add(i);
                    hashMap.put(w, ws);
                }
            }
        }
        PriorityQueue<WordStats> pq = new PriorityQueue<WordStats>(new Comparator<WordStats>(){
            @Override
            public int compare(WordStats w1, WordStats w2){
                if(w1.frequency != w2.frequency){
                    return w2.frequency - w1.frequency;
                }else if(w1.quotesIds.size() != w2.quotesIds.size()){
                    return w2.quotesIds.size() - w1.quotesIds.size();
                }else{
                    return w1.word.compareTo(w2.word);
                }
            }
        });

        for(String w : hashMap.keySet()){
            pq.offer(hashMap.get(w));
        }

        List<String> res = new ArrayList<>();
        while(!pq.isEmpty() && topToys > 0){
            res.add(pq.poll().word);
            topToys--;
        }
        return res;
    }

    static class WordStats{
        int frequency;
        String word;
        Set<Integer> quotesIds;
        public WordStats(String word, int frequency){
            this.word = word;
            this.frequency = frequency;
            quotesIds = new HashSet<>();
        }
    }
}