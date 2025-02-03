#Discount calculation
#Discount = Price * Discount / 100
#final_price = Price - Discount

print("Welcome to the Discount calculator")

Price = int(input("Enter the price of the item:"))

Discount = int(input("Enter the Discount percentage:"))

dis_amount = Price * Discount /100

final_price = Price - dis_amount

print("Cost of the item:",Price)
print("Discount on the item:",Discount,"%")
print("final price after discount:",final_price)