# This takes in 2 input and compares them to each other
#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once
# Ex. restful and fluster

def ana(s1, s2):
    #Check if that the length of each string are the same cause that will show if this is possible
    if len(s1) != len(s2):
        return False

    #We need to convert the string into into a list and sort
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))

    #Now we need to compare them to see if they are the same charcters
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

    
if __name__ == '__main__':

    print(ana("restful", "fluster"))

    