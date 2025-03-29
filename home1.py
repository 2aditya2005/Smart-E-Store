print("---------- View Products -------")
d = {
    1: "Name: Iphone 16, price=85000, model=!!6 pro \n",
    2: "Name: TV 16, price=50000, model=!!6 \n",
    3: "Name: Headphone 16, price=5000, model=!!new \n",
    4: "Name: Camera 16, price=95000, model=!!latest \n",
    5: "Name: Laptop, price=75000, model=!!pavilion \n",
}
print(d)
choice = 0
cart = []
saved_for_later = []

print("------ Menu --------")

while choice != 7:
    print("1) Add to cart")
    print("2) Delete product from cart")
    print("3) Save for later")
    print("4) View cart")
    print("5) Place order")
    print("6) Clear cart")
    print("7) Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Adding item to cart
        product_id = int(input("Enter product ID to add to cart (1-5): "))
        if product_id in d:
            cart.append(d[product_id])
            print(f"Added to cart: {d[product_id]}")
        else:
            print("Invalid product ID.")
    
    elif choice == 2:
        # Deleting item from cart
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}) {item}")
            product_index = int(input("Enter product number to delete from cart: ")) - 1
            if 0 <= product_index < len(cart):
                removed_item = cart.pop(product_index)
                print(f"Removed from cart: {removed_item}")
            else:
                print("Invalid item number.")
    
    elif choice == 3:
        # Saving for later
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in cart:")
            for i, item in enumerate(cart, start=1):
                print(f"{i}) {item}")
            product_index = int(input("Enter product number to save for later: ")) - 1
            if 0 <= product_index < len(cart):
                saved_for_later.append(cart.pop(product_index))
                print(f"Saved for later: {saved_for_later[-1]}")
            else:
                print("Invalid item number.")
    
    elif choice == 4:
        # Viewing the cart
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in cart:")
            for item in cart:
                print(item)
    
    elif choice == 5:
        # Placing order
        if len(cart) == 0:
            print("Your cart is empty. Cannot place order.")
        else:
            print("Order placed successfully!")
            cart.clear()  # Clearing cart after order placement
    
    elif choice == 6:
        # Clearing cart
        if len(cart) == 0:
            print("Your cart is already empty.")
        else:
            cart.clear()
            print("Your cart has been cleared.")
    
    elif choice == 7:
        print("Thank you for visiting! Goodbye!")
    else:
        print("Invalid choice. Please try again.")