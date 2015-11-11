public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> m = new HashMap<>();
        int curLength  = 0;
        int maxLength  = 0;
        int startIndex = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (m.containsKey(ch) && m.get(ch) >= startIndex) {
                startIndex = m.get(ch) + 1;
                curLength = i - startIndex + 1;
            } else if (++curLength > maxLength) maxLength = curLength;
            m.put(ch, i);
        }
        return maxLength;
    }
}
