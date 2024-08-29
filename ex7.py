# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
def count_negative(array):
    count = 0
    for number in array:
        if number== -1:
            count +=1
    return count
number=[-1,11,2,0,-1,4]
print(count_negative(number))