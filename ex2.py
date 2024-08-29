# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sumOddNumber(array):
    sum = 0
    for number in array:
        if number % 2==1:
            sum += number
    return sum
number=[1,2,3,4,5,6,]
sum = sumOddNumber(number)
print(sum)
    
    