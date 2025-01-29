#Programmer: Timothy Pickering
#Date: 1/28/25
#Title: Average Age Calc.

def average_age():#line which calls the function average_age
    print(commonage)#print results
age1 = int(input("Input Age 1:"))#user input
age2 = int(input("Input Age 2:"))#user input
age3 = int(input("Input Age 3:"))#user input
age4 = int(input("Input Age 4:"))#user input
age5 = int(input("Input Age 5:"))#user input
totage = (age1+age2+age3+age4+age5)#sum ages
commonage = totage/5 #average the ages
average_age()#print/display results
