#A palindrome is a string that reads the same forward and backward

word = "radar"

def ispalindrome(w):
    s = list(w)
    n = s[::-1]
    if s == n:
        return True
    else:
        return False

print(ispalindrome(word))