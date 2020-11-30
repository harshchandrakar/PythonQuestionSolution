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

#question 17
wd1 = input('start with D to deposit and W for withdrawl: ').split(',')
D,W = 0,0
for wd in wd1:
    if wd.split(' ')[0] =='D':
        D += int(wd.split(' ')[1])
    elif wd.split(' ')[0]=='W':
         W += int(wd.split(' ')[1])

total = D - W
print(f'total amount in bank : {total}')
