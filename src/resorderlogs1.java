class Solution {
 2       public String[] reorderLogFiles(String[] logs) {
        3        Comparator<String> myComp = new Comparator<String>() {
 4          @Override
 5          public int compare(String s1, String s2) {
                6            String[] split1 = s1.split(" ", 2);
                7            String[] split2 = s2.split(" ", 2);
                8            boolean isDigit1 = Character.isDigit(split1[1].charAt(0));
                9            boolean isDigit2 = Character.isDigit(split2[1].charAt(0));
                10            if(!isDigit1 && !isDigit2) {
                    11              int comp = split1[1].compareTo(split2[1]);
                    12              if(comp != 0)
                        13               return comp;
                    14               return split1[0].compareTo(split2[0]);
                    15            }
                16              return isDigit1 ? (isDigit2 ? 0 : 1) : -1;
                17          }
18        };
        19        Arrays.sort(logs, myComp);
        20        return logs;
        21     }
22 }