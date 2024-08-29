# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
def count_number(array):
    count=0
    for number in array:
        if number == 5:
            count+=1
    return count
number=[2,3,5,0,11,5,2]
print(count_number(number))