// Time complexity: O(n)
// Space complexity: O(1)
bool canPlaceFlowers(vector<int> &flowerbed, int n)
{
    int count = 0;

    for (int i = 0; i < flowerbed.size(); i++)
    {
        if (flowerbed[i] == 0)
        {
            if (i == 0 or flowerbed[i - 1] == 0)
            {
                if (i == flowerbed.size() - 1 or flowerbed[i + 1] == 0)
                {
                    count += 1;
                    flowerbed[i] = 1;
                    if (count == n)
                    {
                        return true;
                    }
                }
            }
        }
    }
    if (count >= n)
    {
        return true;
    }
    else
    {
        return false;
    }
}
