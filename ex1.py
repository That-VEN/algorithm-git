# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum_number(array):
    sum=0
    for number in array:
        sum+= number
    return sum
number=[1,2,3,4,5,6]
print(sum(number))
    
