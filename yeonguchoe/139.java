// Time complexity: O(n^2)
public static boolean wordBreak(String s, List<String> wordDict) {
    int listSize = s.length() + 1;
    boolean[] splittable = new boolean[listSize];
    splittable[0] = true;

    for (int rightPointer = 1; rightPointer < listSize; rightPointer++) {
        for (int leftPointer = 0; leftPointer < rightPointer; leftPointer++) {
            if (splittable[leftPointer] == true && wordDict.contains(s.substring(leftPointer, rightPointer))) {
                splittable[rightPointer] = true;
                break;
            }
        }
    }
    return splittable[s.length()];
}
