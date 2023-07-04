import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {
    public boolean isAnagram(String s, String t) {
      char[] schar = s.toCharArray();
            char[] tchar = t.toCharArray();
            Arrays.sort(schar);
            Arrays.sort(tchar);
            return new String(schar).equals(new String(tchar));
        }
    }
