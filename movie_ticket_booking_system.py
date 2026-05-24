""" Movie Ticket Booking System (freeCodeCamp)

This project handles:
 - Eligibility Checking
 - Membership Verification
 - Ticket Pricing
 - Service Charge Calculation
"""

# Utilize the sys.exit() function to intentionally terminate the Python script
# Picked this up from CS50 Python course and wanted to try it
import sys
import random

def main():
    
    print("------- Movie Ticket Booking System -------")
    print()

    ## Login/Registration Phase ##
    print("-------  1. Login  |  2. Register   -------")
    ch = int(input("Enter your choice (1/2): "))

    if ch == 1:
        # Simulate the actual login process
        # Using random name and age values for testing
        username = input("Username: ")
        password = input("Password: ")
        confirmation = input("Login (Press Enter)")
        if username and password:
            name = random.choice(["Kai", "Gary", "Itachi", "Sasuke", "Ray"])
            age = random.choice([18, 21, 26, 20, 22])
            print(f"Login Successful. Welcome back, {name}!")
            print()
        else:
            sys.exit("Login failed! Please enter both username and password.")

    elif ch == 2:
        # Simulate user registration
        # Collect user information through input
        name = input("Name: ")
        age = int(input("Age: "))
        username = input("Username: ")
        password = input("Password: ")
        confirmation = input("Register (Press Enter)")
        if age < 18:
            sys.exit('Sorry, you are not eligible to register due to age restrictions.')
        else:
            print(f"Registration Successful. Welcome, {name}!")
            print()
    else:
        sys.exit("Wrong Choice.")


    ## Ticket Booking Phase ##
    # base_price, is_weekend, and is_member are predefined values
    base_price = 199
    is_weekend = False
    is_member = True

    # Ask the user for their preferred seat type
    # Apply service charges accordingly
    print("Seat Type | Service Charge:")
    print("1. Premium |  70")
    print("2. Gold    |  40")
    print("3. Regular |  10")
    ch = int(input("Enter your preferred seat type (1/2/3): "))
    if ch == 1: seat_type, service_charges = "Premium", 70
    elif ch == 2: seat_type, service_charges = "Gold", 40
    elif ch == 3: seat_type, service_charges = "Regular", 10
    else: sys.exit("Wrong Choice.")

    # Ask eligible users if they want the evening show
    # Otherwise, randomly assign a morning or night show
    if age >= 21:
        print("You are eligible to apply for the Evening show.")
        print("Do you wish to apply?")
        ch = input("Enter your choice (yes/no): ")
        if ch == 'yes':
            show_time = 'Evening'
        elif ch == 'no':
            show_time = random.choice(["Morning", "Night"])
        else:
            sys.exit("Wrong Choice.")
    else:
        show_time = random.choice(["Morning", "Night"])
    
    # Apply membership discount to eligible users
    if is_member:
        print("A 15% membership discount has been applied.")
        discount = 0.15 * base_price
    else:
        print("You do not qualify for the 15% membership discount.")
        discount = 0
    
    # Calculate extra charges for timing and weekend
    if is_weekend and show_time == 'Evening':
        print("Extra charges will be applied.")
        extra_charges = 0.075 * base_price
    elif is_weekend or show_time == 'Evening':
        print("Extra charges will be applied.")
        extra_charges = 0.05 * base_price
    else:
        print("No extra charges will be applied.")
        extra_charges = 0
    
    total_price = base_price + extra_charges + service_charges - discount
    print(f"Ticket: {name} | {age} | {seat_type} | {show_time} | {round(total_price, 2)}")

if __name__ == "__main__":
    main()