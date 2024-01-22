
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

def unique_num_occurences(arr):
    ht = {}
    checker = set()

    for i in arr:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for val in ht:
        if ht[val] in checker:
            return False
        else:
            checker.add(ht[val])
    return True

def following_key_array(nums, key):
    ht = {}

    for i in range(len(nums)):
        if nums[i] == key and i < len(nums) - 1:
            if nums[i+1] in ht:
                ht[nums[i+1]] += 1
            else:
                ht[nums[i+1]] = 1
    
    high = 0

    most_freq = 0
    high = 0

    for x in ht:
        if ht[x] > high:
            most_freq = x
            high = ht[x]
    return most_freq

def remove_duplicates_inplace(nums):
    k = 1
    if len(nums) == 1:
        return k

    curr = nums[0]
    insert = 1

    for i in range(1, len(nums)): 
        if curr == nums[i] and i < insert:
            insert = i
        if curr != nums[i]:
            curr = nums[i]
            nums[insert] = curr
            k += 1
            insert +=1
    return k

def set_mismatch(nums):
    seen = set()
    dup = 0
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            dup = nums[i]
    for i in range(1, len(nums) + 1):
        if i not in seen:
            return [dup, i]
    
    def search_insert_pos(nums, target):
        # Binary Search -> always return low
        lo, hi = 0, len(nums) - 1
        mid = 0
        
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        

        return lo
        




if __name__ == "__main__":
    n = [11,22,11,33,11,33]

    print(following_key_array(n, 11))

    

    