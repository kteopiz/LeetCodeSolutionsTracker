
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

    # Loop does not stop till right bound of the window exceeds the array
    while high < len(prices):
        # If we find a smaller element than the one at the left than the right, the max profit is found for that element
        if prices[low] > prices[high]:
            low = high
        else:
            # If we are still on the smallest number seen so far, check if a greater profit is made at the right bound of the window
            # Update the profit if necessary
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
        # If we are at the farthest L or R element, we assume the prefix is 1
        if i == 0:
            # For the first prefix, assign a value dont multiply as the array intialized as zeros
            result[i] = pre
        else: 
            pre *= nums[i - 1]
            # Same as here, assign a value dont multiply
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

def can_place_flowers(flowerbed, n):
    if len(flowerbed) == 1 and n > 0:
            if flowerbed[0] == 1: # n <= 1
                return False
            elif flowerbed[0] == 0 and n == 1:
                return True

    for i in range(len(flowerbed)):
        if n == 0:
            return True
        # 2 Edge Cases at either end of the flowerbed
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
    return n <= 0

if __name__ == "__main__":
    n = [1,0,0,0,1,0,0]

    print(can_place_flowers(n, 2))

    

    