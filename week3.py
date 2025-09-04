orign_price = int(input("Enter original price: "))
discount_percentage = float(input("Enter discount percentage: "))

def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

if discount_percentage > 20:
    discounted_price = calculate_discounted_price(orign_price, discount_percentage)
    print(f"Discounted price: {discounted_price}")
else:
    print(f"Original price: {orign_price}")
 