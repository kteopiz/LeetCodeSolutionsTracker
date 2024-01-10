
def is_palindrome(x):
    # Two Pointers at the beginning and end of the Palindrome
        xString = str(x)
        start = 0
        end = len(xString) - 1


        # -> 1 0 1 <-
        while start <= end:
            if xString[start] != xString[end]:
                return False
            else:
                start += 1
                end -= 1
        return True 

def length_of_longest_substring(s):
    slow, fast, longest = 0,0,0

    letter_set = set()

    # Edge Cases for smaller strings
    if len(s) == 0:
         return 0
    elif len(s) == 1:
         return 1

    while fast < len(s):
        if s[fast] in letter_set:
            # if the length of the current substring is greatest, save it
            if longest < len(letter_set):
                longest = len(letter_set)
            # Remove the already seen letter and push the window one over so the set is valid and represents the window's contents
            letter_set.remove(s[slow]) 
            slow += 1
        else:
             # If the letter is unique, add it to the set and slide the right bound of the window
             letter_set.add(s[fast])
             fast += 1
    
    # Covers for two cases:
             # 1) Where the string is completely unique, the set will hold the true value of longest substring as it will not be updated
             # 2) When the longest substring ends on the last letter of the string, the set will also hold the true value of the longest substring and will not be updated
    if longest < len(letter_set):
         return len(letter_set)
    else:
         return longest

if __name__ == "__main__":
    pass
    





