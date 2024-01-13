
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

def product_except_self(nums):
    # Two Pass Approach -> Calculate prefix then postfix products of each position
    result = [0 for x in range(len(nums))]
    pre = 1
    post = 1

    for i in range(len(nums)):
        if i == 0:
            result[i] = pre
        else: 
            pre *= nums[i - 1]
            result[i] = pre
    
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) -1:
            result[i] *= post
        else:
            post *= nums[i + 1]
            result[i] *= post
    return result

def contains_duplicate(nums):
    ht = set()

    if len(nums) < 2:
        return False

    for i in nums:
        if i in ht:
            return True
        else:
            ht.add(i)
    return False

if __name__ == "__main__":
    n = [5,9,2,-9,-9,-7,-8,7,-9,10]

    print(product_except_self(n))

    

    