#question 16
numbers = input('enter numbers : ').split(',')
square_num = []
for num in numbers:
    if int(num) %2 != 0:
        square_num.append(f'{int(num)**2}')
squared_numbers = ','.join(square_num)
print(squared_numbers)
 # or integrated form
squared_number = [f'{int(num)**2}' for num in input('enter numbers: ').split(',') if int(num)%2 != 0]
odd_squares = ','.join(squared_number)
print(odd_squares)
