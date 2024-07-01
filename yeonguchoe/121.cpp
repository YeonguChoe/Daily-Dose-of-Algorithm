// Leet Code 121: Best Time to Buy and Sell Stock

// Time complexity: O(n): Iteration over prices arrays
// Space complexity: O(1): days, min_price, result
int maxProfit(vector<int>& prices)
{
    int days = prices.size();
    int min_price = INT_MAX;
    int result = 0;
    for (int i = 0; i < days; i++)
    {
        if (prices[i] < min_price)
        {
            min_price = prices[i];
        }
        else if (prices[i] - min_price > result)
        {
            result = prices[i] - min_price;
        }
    }
    return result;
}
