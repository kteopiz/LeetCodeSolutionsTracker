import java.util.*;

public class arraysAndStrings {


/*
 * Name: 1768 Merge Strings Alternaely
 * Diff: Easy
 */

 public String mergeAlternately(String word1, String word2) {

    // StringBuilder allows a mutable String like object
    StringBuilder result = new StringBuilder();
    int FL = word1.length();
    int SL = word2.length();
    int i = 0;
    int j = 0;

    // while loop does not stop until both counters have fully traversed their own words
    while (i < FL || j < SL) {
        // if we are still in either word continue to append and go on to the next word
        if (i < FL) {
            result.append(word1.charAt(i));
            i++;
        }
        if (j < SL) {
            result.append(word2.charAt(j));
            j++;
        }
    }

    return result.toString();


}

}






