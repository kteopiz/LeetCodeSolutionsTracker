
def first_bad_version(n):

    """
    **IMPORTANT** This cannot be run here since we do not have the code for the isBadVersion API, however valid solution on LC Site
    """

    lo = 0
    hi = n
    
    # Edge Case: If n == 1 and there is always at least 1 bad version
    if n == 1:
        return n

    # Binary Search with 3 Cases
    while lo < hi:
        mid = (hi + lo) // 2
        # Found a bad but a bad exists before it, traverse lower
        if isBadVersion(mid) and isBadVersion(mid - 1):
            hi = mid - 1
        # Found a good with a good in front of it, traverse higher
        elif not isBadVersion(mid) and not isBadVersion(mid + 1):
            lo = mid + 1
        # Found a good with a bad in front of it we return the bad's positon
        elif not isBadVersion(mid) and isBadVersion(mid+1):
            return mid + 1
        # We found a bad and behind it is a good, we are on the first bad version
        else:
            return mid
            





if __name__ == "__main__":
    pass