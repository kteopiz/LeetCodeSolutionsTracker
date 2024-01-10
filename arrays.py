
def two_sum(nums, target):
     # HashMap used to track elements we have seen so far and map them to their index number
        ht = {}
        
        for i in range(len(nums)):
            # Can return an answer if the current element's complement is in the hash table
            if target - nums[i] in ht:
                return [i, ht[target - nums[i]]]
            # if it is not, add it to the hashmap to use for checking the complement of future elements
            else:
                ht[nums[i]] = i

def best_time_buy_stock(prices):
    low, high, profit = 0,1,0

    # Edge Case: If only one price in the array, no profit can be made
    if len(prices) == 1:
        return profit

    while high < len(prices):
        if prices[low] > prices[high]:
            low = high
        else:
            if profit < prices[high] - prices[low]:
                profit = prices[high] - prices[low]
        high += 1
    
    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(best_time_buy_stock(prices))