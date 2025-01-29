#Programmer: Timothy Pickering
#Date: 1/28/2025
#Title: Purchase Total

def calculate_total_purchase():
    print("Subtotal:$", subtotal, "Tax:$", tax, "Total:$", total)
item1 = int(input("Item 1 Price:"))
item2 = int(input("Item 2 Price:"))
item3 = int(input("Item 3 Price:"))
item4 = int(input("Item 4 Price:"))
item5 = int(input("Item 5 Price:"))
subtotal = (item1+item2+item3+item4+item5)
tax = (subtotal*0.07)
total = (subtotal+tax)
calculate_total_purchase()
