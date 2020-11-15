public class favgenres1 {
    public static Map<String, List<String>> favoriteGenre(Map<String,List<String>> userMap, Map<String, List<String>> genreMap) {
        // key is song, value is genre
        HashMap<String, String> songToGenre = new HashMap<>();
        for(String genre : genreMap.keySet()){
            List<String> songs = genreMap.get(genre);
            for(String song : songs){
                songToGenre.put(song, genre);
            }
        }
        Map<String, List<String>> res = new HashMap<>();

        for(String user: userMap.keySet()){
            HashMap<String, Integer> count = new HashMap<>();
            List<String> songs = userMap.get(user);
            int max = 0;
            res.put(user, new ArrayList<>());
            for(String song : songs){
                count.put(songToGenre.get(song), count.getOrDefault(songToGenre.get(song), 0) + 1);
                max = Math.max(max, count.get(songToGenre.get(song)));
            }
            for(String genre : count.keySet()){
                if(count.get(genre) == max){
                    res.get(user).add(genre);
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
        Map<String, List<String>> userSongs = new HashMap<>();
        List<String> list1 = Arrays.asList("song1", "song2", "song3", "song4", "song8");
        List<String> list2 = Arrays.asList("song5", "song6", "song7");
        userSongs.put("David", list1);
        userSongs.put("Emma", list2);

        Map<String, List<String>> songGenres = new HashMap<>();
        List<String> list3 = Arrays.asList("song1", "song3");
        List<String> list4 = Arrays.asList("song7");
        List<String> list5 = Arrays.asList("song2", "song4");
        List<String> list6 = Arrays.asList("song5", "song6");
        List<String> list7 = Arrays.asList("song8", "song9");
        songGenres.put("Rock", list3);
        songGenres.put("Dubstep", list4);
        songGenres.put("Techno", list5);
        songGenres.put("Pop", list6);
        songGenres.put("Jazz", list7);

        System.out.println(favoriteGenre(userSongs, songGenres));
    }
}
