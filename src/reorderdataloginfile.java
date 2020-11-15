public class reorderdataloginfile {
    public String[] reorderLogFiles(String[] logs) {
        if(logs == null || logs.length == 0){
            return new String[]{};
        }

        Comparator<String> logComparator = new Comparator<String>(){
            public int compare(String s1, String s2){
                int index1 = s1.indexOf(" ");
                int index2 = s2.indexOf(" ");
                boolean isDigit1 = Character.isDigit(s1.charAt(index1 + 1));
                boolean isDigit2 = Character.isDigit(s2.charAt(index2 + 1));

                // letter order is lexicographically order
                if(!isDigit1 && !isDigit2){
                    int compare = s1.substring(index1 + 1).compareTo(s2.substring(index2 + 1));
                    // if equal, compare identifer
                    if(compare == 0){
                        return s1.substring(0, index1).compareTo(s2.substring(0, index2));
                    }
                    return compare;
                }else if(isDigit1 && isDigit2){
                    // both are digit logs
                    return 0;
                }else if(isDigit1 && !isDigit2){
                    // s2 is letter
                    return 1;
                }else{
                    // s1 is letter
                    return -1;
                }
            }
        };

        Arrays.sort(logs, logComparator);

        return logs;
    }
}
