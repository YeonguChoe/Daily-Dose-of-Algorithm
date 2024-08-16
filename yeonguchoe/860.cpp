// Time complexity: O(n)
// Space complexity: O(n)
bool lemonadeChange(vector<int> &bills)
{
    // 지폐의 개수를 세기 위해, (지폐 -> 장수) 를 매핑해주는 change 맵을 만듬
    unordered_map<int, int> change = {{5, 0}, {10, 0}, {20, 0}};
    for (int bill : bills)
    {
        // 현재 지폐를 기준으로 장수 증가
        change[bill] += 1;
        // 만약에 현재 지폐가 10달러권이면, 5달러권에서 1개 뺌
        if (bill == 10)
        {
            change[5] -= 1;
        }
        // 만약에 현재 지폐가 20달러권이면,
        else if (bill == 20)
        {
            // 10달러권이 있는경우, 10달러권 1개와 5달러권 1개를 뺌
            if (change[10] > 0)
            {
                change[10] -= 1;
                change[5] -= 1;
            }
            // 10달러권이 없는 경우, 5달러권에서 3개를 뺌
            else
            {
                change[5] -= 3;
            }
        }
        // 만약에 5달러권이 맵에서 음수이면, 매개변수로 주어진 순서로 결제를 받았을때 거스름돈을 줄수가 없는 경우가 존재.
        if (change[5] < 0)
        {
            return false;
        }
    }
    return true;
}
