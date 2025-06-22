def calculate_total_price(item_price, quantity):
    item_total = item_price * quantity
    tax_rate = 0.07
    tax_amount =item_total * tax_rate
    total_price = item_total + tax_amount
    return total_price 
    discount = 0.1
    discounted_price = total_price - (total_price * discount)

item_price = 25.0
quantity = 4
print("Total Price:",calculate_total_price(item_price, quantity))