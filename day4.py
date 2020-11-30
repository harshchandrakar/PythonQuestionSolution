#question 14

sentence = input('Write a sentence to check number of upper case and lowercase letter: ')

UPPERCASE,LOWERCASE = 0,0

for i in list(sentence):
    if 'A'<= i <='Z' :
        UPPERCASE += 1
    elif 'a'<= i <='z':
        LOWERCASE +=1

print(f'number of uppercase letters = {UPPERCASE} \n number of lower case letters = {LOWERCASE}')

# question 15
a = input('Set the value of a : ')

value = int(a)*(1234) #1+11+111+1111

print(f'value of a + aa + aaa + aaaa = {value}')

or
a = input('Set the value of a : ')

value = int(a)+int(2*a)+int(3*a)+int(4*a)

print(f'value of a + aa + aaa + aaaa = {value}')
