
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
    
def merge_alternately(word1, word2):
    result = ""
    # Recursively take one letter off each word
    # In the case where one word is shorter than the other, return the existing result plus the rest of the other word -> no more alternation
    if len(word1) > 0 and len(word2) > 0:
        result += word1[0] + word2[0]
        return result + merge_alternately(word1[1:], word2[1:])
    elif len(word1) == 0:
        return result + word2
    else: 
        return result + word1

def roman_to_int(s):
    # Save all values in a hashtable for effecient access and checking
    ht = {
        "I": 1,
        "IV" : 4,
        "V":5,
        "IX": 9,
        "X":10,
        "XL":40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000 }
    # left and right create a sliding window of the two current elements
    left = 0
    right = 1
    result = 0

    # if the length of the string is less than 2, there is only single letter values possible
    if len(s) < 2:
        return ht[s[left]]
    
    # We include right because it can be at most one index past the array which == len(s)
    while left < len(s) and right <= len(s):
        # Odd Number Case, reached end of string
        if right >= len(s):
            result += ht[s[left]]
            return result
        # Checking if the current window is a valid 2 letter value
        if s[left] + s[right] in ht:
            result += ht[s[left] + s[right]]
            # If so we push the window completely past it 
            left += 2
            right += 2
        else:
            # If we only have a valid single value, it is on the left of the window, we increment one to check the next pair
            result += ht[s[left]]
            left += 1
            right += 1
    
    return result

def first_letter_twice(s) -> str:
    check = set()

    for i in s:
        if i in check:
            return i
        else:
            check.add(i)


     

if __name__ == "__main__":
    print(not False and not False)
    





