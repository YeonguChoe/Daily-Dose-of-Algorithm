// Time complexity: O(n)
// Space complexity: O(1)
int lengthOfLastWord(string& s)
{
    int pointer = s.length() - 1;
    int length = 0;

    while (pointer >= 0 and s[pointer] == ' ') // 문자가 1개일때 s[pointer] ==' '에 의해 여기서 잡힘
    {
        pointer--;
    }

    while (pointer >= 0 and s[pointer] != ' ') // 처음으로 문자를 만나면 length 세기 시작
    {
        length++;
        pointer--;
    }
    return length;
}
