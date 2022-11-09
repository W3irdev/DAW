"""1. Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages."""


"""for i in range(1,101):
    if i%13 == 0 and i%7==0:
        print(f"The number {i} is a multiple of 7 and 13")
    elif i%7==0:
        print(f"The number {i} is a multiple of 7")
    elif i%13==0:
        print(f"The number {i} is a multiple of 13")
    else:
        print(i)

"""

"""2. Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
…..
7*10=70"""

""""entrada=int(input("Enter a number between 0 and 10: "))

if 10>entrada>0:
    for i in range(0,11):
        print(f"{entrada}*{i}={entrada*i}")
else:
    print("The number is out of the boundaries")"""


"""3. Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”
"""

"""cant=int(input("How many numbers do you want input? "))
contador=0
while cant <=0:
    cant=int(input("How many numbers do you want input? "))
while contador < cant:
    peti=int(input("Enter one number greater than 0: "))
    while peti <=0:
        peti=int(input("The number is not valid, it should be greater than 0: "))
    if peti%2==0:
        print(f"The number {peti} is even")
    else:
        print(f"The number {peti} is odd")
    contador+=1"""

"""4. Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. If the number N is not valid, the
program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.”
"""
"""sumatoria=0
num1=int(input("Enter one number greater than 0: "))
while num1 < 1:
    num1=int(input("The number is not right, try again. "))
else:
    for i in range(num1):        
        sumatoria=sumatoria+i
        print(sumatoria)
    print(f"The sum of the N first numbers is {sumatoria+num1}")"""

"""5. Design a program that asks for numbers until the user inputs a negative one. When
this happens, the program will show how many positive numbers have been
introduced by the user. The messages are the following:
“Enter a number (negative to finish):”
“You have entered XX positive numbers.”"""

"""num1=0
contador=0
while num1 >=0:
    num1=int(input("Enter a number (negative to finish): "))
    contador+=1

print(f"You have entered {contador-1} positive numbers.")
"""
"""6. Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
“Enter one number:”
“The product is XX”
"""

"""num1=int(input("Enter one number: "))
num2=int(input("Enter one number: "))
contador=0
producto=0
while contador < num2:
    producto+=num1
    contador+=1
print(f"The product is {producto}")"""

"""7. Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The medium is XX.XX” to show the result.
"""
"""try:
    num1=int(input("Cuantos numeros desea introducir?: "))
    contador=0

    memo1=0
    while contador < num1:
        memo=0
        nums=int(input("Escribe numeros mayores que 0: "))
        if nums >0:            
            memo=nums
            contador+=1
        else: print("Numeros mayor que 0")
        memo1+=memo
        media=memo1/num1
    print(media)
except:
    print("Introduce un nº mayor de 0")"""

"""8. Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
"""

memo=int(input("Enter one number: "))
while True:
    afirmacion=input("Do you want to enter more numbers (Y/N)?\n").upper()
    if afirmacion == "Y":
        num1=int(input("Enter one number: "))
        if num1 < memo:
            memo=num1
    elif afirmacion =="N":
        print(f"The smallest number is {memo}")
        break
    else:
        print("Introduzca Y/N")

"""9. Design a program that reads an integer positive number greater than 0 and says if
its a “perfect number”. A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect.”"""

"""try:
    num1=int(input("Enter an integer positive number greater than 0: "))
    divisores=[]
    for i in range(1,num1):
        if num1%i==0:
            memo=i
            divisores.append(memo)

    if num1 <=0: print("The number is not valid, try again.")
    elif (sum(divisores)) == num1:
        print(f"the number {num1} is perfect")
    else:
        print(f"The number {num1} is not perfect")
except:
    print("The number is not valid")"""

#Opcion sin lista
"""num1=int(input("Enter an integer positive number greater than 0: "))
memo=0
for i in range(1,(num1//2)+1):
    if num1%i==0:
        memo+=i
if memo == num1:
    print(f"the number {num1} is perfect")
else:
    print(f"The number {num1} is not perfect")"""

"""10. Design a program that reads an integer positive number and says the “factorial” of
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX”"""

"""num1=int(input("Enter an integer positive number: "))

while num1 <=0:
    num1=int(input("The number is not valid, try again. "))

fact=num1
while num1 > 1:
    num1-=1
    fact=fact*num1
print(f"The factorial is {fact}")"""