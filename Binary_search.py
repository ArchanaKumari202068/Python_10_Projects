# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop 
# increase the steps each time a split is done
# conditions to track target position 
#example: [1,2,3,4,5,6,7,8,9,10] target = 3
# (0+9)/2=4.5 check 3 is gt than or less than 4.5
#[1,2,3,4,5]

def binary_search(list,element):
    middle = 0           # var
    start = 0
    end = len(list)
    steps = 0
    while(start<=end):
        print("Steps",steps,":",list[start:end+1]) # display list from start to end
        steps = steps+1
        middle = (start + end )//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle -1
        else :
            start = middle +1

            # [1,2,3,4,5]4
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12
binary_search(my_list,target) 


