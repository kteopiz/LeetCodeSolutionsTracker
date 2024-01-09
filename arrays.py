
def twosum(nums, target):
     # HashMap used to track elements we have seen so far and map them to their index number
        ht = {}
        
        for i in range(len(nums)):
            # Can return an answer if the current element's complement is in the hash table
            if target - nums[i] in ht:
                return [i, ht[target - nums[i]]]
            # if it is not, add it to the hashmap to use for checking the complement of future elements
            else:
                ht[nums[i]] = i

if __name__ == "__main__":
    pass