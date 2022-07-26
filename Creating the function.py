#wpp functio to create calculator

#creating the function

def addition(num1,num2): 
    add= num1+num2
    print(add)

#substraction functiom

def substraction(num1,num2):
    sub=num1-num2
    print(sub)

#division function

def division(num1,num2):
    div=num1/num2
    print(div)

#multipication function

def multiplication(num1,num2):
    multi=num1*num2
    print(multi)


#Calling the function

n1= float(input("Enter the first number"))
n2= float(input("Enter the second number"))

addition(n1,n2)
substraction(n1,n2)
division(n1,n2)
multiplication(n1,n2)
