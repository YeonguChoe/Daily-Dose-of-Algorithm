class Solution {
public:
    bool isSubsequence(string s, string t) {

        // s가 공백인 경우
        if (s == "") {
            return true;
        }

        // s의 각 char을 가리키는 포인터
        int ptr = 0;

        for (char c : t) {
            if (c == s[ptr]) {
                ptr++;
            }
            if (ptr == s.size()) {
                return true;
            }
        }
        return false;
    }
};
