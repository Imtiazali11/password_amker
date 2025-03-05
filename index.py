# Define the menue of the restaurant
# menu = { 
#     'pizza' : 40,
#     'Pasta' : 50,
#     'burger' : 70,
#     'Slaad' : 60,
#     'Coffee' : 80
# }
# # Greet

# print("Welcome to the python Restaurant")
# print("Pizza : Rs40\nPasta: Rs50\n burger:70\n salad:60\n coffee:80")
# print(menu)
def restaurant_menu():
    menu = {
        'Pizza': 40,
        'Pasta': 50,
        'Burger': 70,
        'Salad': 60,
        'Coffee': 80
    }
    
    print("Welcome to the Python Restaurant!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")
    
    return menu

# Run the function
restaurant_menu()


