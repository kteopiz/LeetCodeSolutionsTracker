def topKFrequent(nums, k):
    def partition(arr, lo, hi, ht):
        i = lo
        j = hi - 1
        pivot = ht[arr[hi]]
        while i < j:
            while i < hi and ht[arr[i]] > pivot:
                i += 1
            while j > lo and ht[arr[j]] <= pivot:
                j -= 1
            if i < j:
                (arr[i], arr[j]) = (arr[j], arr[i])
            
        if ht[arr[i]] < pivot:
            (arr[hi], arr[i]) = (arr[i], arr[hi])
        return i

    def quicksort(arr, left, right, ht):
        if left < right:
            split_pos = partition(arr, left, right, ht)
            quicksort(arr, left, split_pos - 1, ht)
            quicksort(arr, split_pos + 1, right, ht)
        return arr
    ht = {}
    res = []
    for i in nums:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    keys = list(ht.keys())
    res = quicksort(keys, 0, len(keys) - 1, ht)
    return res[0: k]

def optimize_top_k(nums, k):
    ht = {}
    bucket = [[]] * len(nums)
    res = []
    for i in nums:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in ht:
        bucket[ht[i] - 1].append(i)
        print(ht)
    print(bucket)
    j = len(bucket) - 1
    while len(res) < k:
        if len(bucket[j]) > 0 and len(res) < k:
            for i in range(len(bucket[j])):
                res.append(bucket[j][i])
        j -= 1
    return res

def word_search(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()
    
    # seek is the index of the char in word we are looking for
    def dfs(r, c, seek):
        if seek == len(word):
            return True 
        elif r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in path or word[seek] != board[r][c]:
            return False
        # We have made it past the last letter of the word
        seek += 1
        path.add((r, c))
        res = (dfs(r - 1, c, seek) or dfs(r + 1, c, seek) or dfs(r, c - 1, seek) or dfs(r, c + 1, seek))
        path.remove((r, c))
        return res

    for i in range(ROWS):
        for j in range(COLS):
            found = dfs(i, j, 0)
            if found:
                return True
    return False



    


if __name__ == "__main__":
    board = [['a', 'b'], ['c', 'd']]
    print(word_search(board, "abd"))