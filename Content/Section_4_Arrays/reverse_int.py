# Reverse a int 
# input: 1234
# output: 4321

def rev(x):
    out = 0

    #This will check that the remainding sum if it has finish the process
    while x > 0:
        # This will give my the most right hand digit
        mod = x % 10
        #This will times 10 if the old total making moving one place value over the will add the mod to the end
        out = (out*10) + mod
        #This will divide by 10 with no remainder
        x = x // 10

    return out

if __name__ == '__main__':
   
    print(rev(12345))