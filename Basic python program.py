#1.python program to print your name
n="v.abhishek"
print(n)

#2.get the input from the user and print
name = input("enter your name")  
print(name)     

#3.get the input from userand print it
num1=input("enter your first number")
num2=input("enter your second number")
print("first number:",num1)
print("second number:",num2)

#4.get the input from user add two number
num3=int(input("enter your third number"))
num4=int(input("enter your fourth number"))
sum=num3+num4
print("sum of two values:",sum)

#5.genrate first name and last name
a=input("enter the first name")
b=input("enter the second name")
c=a+b
print("your full name:",c)

#6.Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
a=a+b
b=a-b
print("a",a)
print("b",b)

#7.Write a python  programee get a input from user swap 2 numbers withour 3rd variable
a=10
b=20
temp=a
a=b
b=temp
print("after swapping:",a)
print("after swapping:",b)

#8.write a python program print the primitive data type
a=10
b=2.13
c=True
print("interger is :",a)
print("float is :",b)
print("Boolean is ",c)

#9.write a python program print the non primitive data type
a=(10,20,30)
b=[10,10,20,30]
c={10,20,20,30}
dict_1={"one":1,"two":2}
print(a)
print(b)
print(c)
print(dict_1)

#10.write a python to square of a number
a=int(input("Enter a number:"))
Square=a*a
print("Square of a number:",Square)

#11.find the avg of 3 number you have to get input from the user
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
avg=(a+b+c)/3
print("Average is:",avg)

#12.write a python program to take a num as any user and multiplied by 10
a=int(input("Enter a number:"))
b=a*10
print("After multipying with 10:",b)

#13.write a python program to covert min into sec
a=int(input("Enter Minutes"))
sec=a*60
print("Seconds=",sec)

#14.write a python program to floating points
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
Product=a*b
print("Product=",Product)

#15.largest of three numbers
a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
c=float(input("Enter Third Number:"))
largest_number=max(a,b,c)
print("Largest number is:",largest_number)

#16.sum of first n natural number
n=(int(input("Enter input=")))
sum=n*(n+1)
print("Sum=",sum)

#17.arthimatic
a=10
b=20
print("addition=",a+b)
print("Subtration=",a-b)
print("Multiplication=",a*b)
prinBasic python program.py
￼
t("Module division=",a%b)

#18.logical operator
a=10
b=12
print(a>0 and b>15)
print(a>15 or b>5)
print(not(a==10))


#19.write a python program to print positive and negitive and zero
a=int(input("enter the number"))
if a>0:
    print("positive")
elif a<0:
    print("negitive")
else:
    print("zero")        

#20.write a python program even and odd
a=int(input("enter the number"))
if (a%2==0):
    print("number is even")
else:
    print("number is odd")    


#21.write a python program to check the number is divisible by 5 and 11
a=int(input("enter the number"))
if (a%5==0 and a%11==0):
    print("the number is divisible by 5 and 11")
else:
    print("the number is not dividible") 

#22.Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

n = int(input("Enter the operation number (1-4): "))

if n == 1:
    print("Result:", a + b)
elif n == 2:
    print("Result:", a - b)
elif n == 3:
    print("Result:", a * b)
elif n == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation number")


#23.Program to check the day of the week based on user input
week = int(input("Enter the week number (1 for Monday, 7 for Sunday): "))

if week == 1:
    print("MONDAY")
elif week == 2:
    print("TUESDAY")
elif week == 3:
    print("WEDNESDAY")
elif week == 4:
    print("THURSDAY")
elif week == 5:
    print("FRIDAY")
elif week == 6:
    print("SATURDAY")
elif week == 7:
    print("SUNDAY")
else:
    print("Invalid input! Please enter a number between 1 and 7.")   



    
#24.write a python program to print the days_months

m = int(input("Enter the month number (1-12): "))

if m == 2:
    print("28 or 29 days")
elif m in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif m in [4, 6, 9, 11]:
    print("30 days")
else:
    print("Invalid month number")  


    
#25.write a python program to check the body temperature(FEVER,NORMAL&COLD)

temp = int(input("Check the body temperature: "))

if temp >= 100:
    print("FEVER")
elif 97 <= temp <= 99:
    print("NORMAL")
elif temp < 97:
    print("COLD")
else:
    print("Invalid temperature")



#26.write a python program to give the vote eligible for a person

v = int(input("Enter your age: "))

if v >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#27. Program to check username and password credentials

user = "V.Abhishek"
password = 1234
username = input("Enter your username: ")

if username != user:
    print("Invalid username")
else:
    password_input = int(input("Enter your password: "))

    if password_input == password:
        print("Login successful")
    else:
        print("Invalid password")  


#28.program to assign grades based on marks
m = int(input("Enter your marks: "))

if m >= 90:
    print("Grade A")
elif m >= 80:
    print("Grade B")
elif m >= 60:
    print("Grade C")
elif m >= 50:
    print("Grade D")
else:
    print("FAIL") 

#29.student  pass and exam if they score at least 35 marks in theory and 50  marks in pratical. if  they score is more than 60marks total
theory_marks=int(input("enter theory marks"))
pratical_marks=int(input("enter pratical marks"))
total_marks=theory_marks+pratical_marks
if theory_marks>=35 and pratical_marks>=50 and total_marks>60:
    print("student passed")
else:
    print("student failed")   



#30.a person can acess an atm onli if they insert atm enter the correct pin the account not locked
atm_card_inserted = True
correct_pin = True
acc_locked = False

if atm_card_inserted and correct_pin and not acc_locked:
    print("Access Granted: you can use the ATM")
else:
    print("Access Denied: ATM access not allowed")


