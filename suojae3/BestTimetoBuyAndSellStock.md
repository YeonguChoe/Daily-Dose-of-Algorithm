## Best Time to Buy And Sell Stock
link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

<br/>


### Swift

#### 1차시도
- 2중 for문 돌려서 두날짜의 가격 뺀값을 sum에 넣어서 리턴
- 시간복잡도 n^2으로 인한 시간초과
  
```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var sum = 0
        
        for i in 0..<prices.count-1 {
            for j in i+1..<prices.count {
                guard prices[j] + prices[i] > 0 else { continue }
                guard sum < prices[j] - prices[i] else { continue }
                sum = prices[j] - prices[i]
            }
        }
        return sum
    }
}
```

<br/>

#### 2차시도
- 저렴할 때 사서 비쌀 때 파는걸 그래프로 상상하면 결국 높이가 가장 긴 것을 구해야한다는 힌트를 얻음

```swift
class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minPrice = Int.max
        var answer = 0
        
        for value in prices {
            if value < minPrice  {
                minPrice = value
            } else if value - minPrice > answer {
                answer = value - minPrice
            }
        }
        return answer
    }
}
```
  


<br/>

#

### Dart 답안

```dart
class Solution {
  int maxProfit(List<int> prices) {
    int minValue = (1 << 63) - 1;
    int answer = 0;

    for (int value in prices) {
      if (value < minValue) {
        minValue = value;
      } else if (answer < value - minValue) {
        answer = value - minValue;
      }
    }

    return answer;
  }
}
```
