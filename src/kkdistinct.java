// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
import java.util.*;

// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class Solution
{
    // METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
    public List<String> subStringsKDist(String inputStr, int num)
    {
        // WRITE YOUR CODE HERE
        int distinct=0,i=0;
        int [] memo=new int[26];
        Set<String> set=new HashSet<>();
        for (;i<num;i++){
            if (memo[inputStr.charAt(i)-'a']==0)
                distinct+=1;
            memo[inputStr.charAt(i)-'a']+=1;
        }
        if (distinct==num) {
            set.add(inputStr.substring(i-num,i));
        }
        while (i<inputStr.length()){
            if (memo[inputStr.charAt(i)-'a']==0)
                distinct+=1;
            memo[inputStr.charAt(i)-'a']+=1;
            memo[inputStr.charAt(i-num)-'a']-=1;
            if (memo[inputStr.charAt(i-num)-'a']==0)
                distinct-=1;
            if (distinct==num)
                set.add(inputStr.substring(i-num+1,i+1));
            i+=1;
        }

        return new ArrayList<>(set);
    }
    // METHOD SIGNATURE ENDS
}
if (columnCount ==0 && rowCount==0)
    return