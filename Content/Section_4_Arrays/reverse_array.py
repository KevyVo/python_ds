l1 = [1,2,3,4,5,6,7,8,9]

# Reverse a list of number backwards
def reverseX(x):
    newL = []
    #Will count the loops it need to iterate
    for i in range(len(x)):
        #Will now Add the old list to the new single list object number
        newL = newL + [x[(len(x)-(i+1))]]
    return newL

#Udemy solution
def reverse(nums):

    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1


if __name__ == '__main__':

    n = [-3, 0, 3]
    reverse(n)
    print(n)

print(reverseX(l1))
