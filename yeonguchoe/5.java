// Time complexity: O(n^2)
// Space complexity: O(n^2)

public String longestPalindrome(String s) {
        String currentLongest = "";

        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i;

            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 > currentLongest.length()) {
                    currentLongest = s.substring(left, right + 1);
                }
                left -= 1;
                right += 1;
            }

            left = i;
            right = i + 1;

            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 > currentLongest.length()) {
                    currentLongest = s.substring(left, right + 1);
                }
                left -= 1;
                right += 1;
            }
        }

        return currentLongest;
    }
