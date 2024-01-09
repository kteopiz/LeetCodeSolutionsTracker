
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
def lengthOfLongestSubstring(s):

        letter_set = set()

        longest, slow, fast = 0, 0, 0

        # Edge Cases for small strings
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        while fast < (len(s)):
            if s[fast] in letter_set:
                # Save length of longest substring if it is larger than the current max length substring
                if len(letter_set) > longest:
                    longest = len(letter_set)
                # Reset the letter set
                letter_set = set()
                # Pull the slow pointer forward to check
                slow = fast
            else:
                letter_set.add(s[fast])
                fast += 1
        print(letter_set)
        if longest < len(letter_set):
             return len(letter_set)
        else:
             return longest

if __name__ == "__main__":
    # Current Case does not work couple ideas on why:
    # 1) Set updation -> Right now we are totally resetting the set once we find a duplicate ...
    # Achieve this by jumping the slow poitner to the fast one, this skips over a letter that belongs to the longest substring
    # Currently -> 407/987 test cases passing on LC
    s = "dvdf"

    print(lengthOfLongestSubstring(s))
    





