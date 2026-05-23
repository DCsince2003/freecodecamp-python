#Movie Ticket Booking System Project (freeCodeCamp)
'''
This Project automates the ticket booking system
from the initial eligibility check to membership verification
and final price calculation after various charges and discount
'''

def main():
    # line 10 - 15 are there to initialize the variables
    base_price = 15
    age = 21
    is_member = False
    is_weekend = False
    seat_type = 'Gold'
    show_time = 'Evening'
    
    # line 18 - 21 ensure only eligible users book the ticket
    if age > 17:
        print('User is eligible to book a ticket')
    else:
        print('User is not eligible to book a ticket')
    
    # line 24 - 27 ensure eligible user could apply for their preferred show timing
    if age >= 21:
        print('User is eligible for Evening shows')
    else:
        print('User is not eligible for Evening shows')
    
    # line 30 - 36 ensure members can avail the membership discount
    discount = 0
    if is_member and age >= 21:
        discount = 3
        print('User qualifies for membership discount')
    else:
        print('User does not qualify for membership discount')
    print('Discount:', discount)
    
    # line 39 - 45 calculate the extra charges for weekends and preferred show timings
    extra_charges = 0
    if is_weekend or show_time == 'Evening':
        extra_charges = 2
        print('Extra charges will be applied')
    else:
        print('No extra charges will be applied')
    print('Extra charges:', extra_charges)
    
    # lines 48 re-checks the above conditions (gotta work on that)
    if age >= 21 or age >= 17 and (show_time != 'Evening' or is_member):
        print('Ticket booking condition satisfied')

        # line 53 - 60 calculates the service charge
        # based on the type of seat they want
        service_charges = 0
        if seat_type == 'Premium':
            service_charges = 5
        elif seat_type == 'Gold':
            service_charges = 3
        else:
            service_charges = 1
        print('Service charges:', service_charges)
        
        # Now, we calcualte and display the final price
        final_price = base_price + extra_charges + service_charges - discount
        print("Final price of ticket:",final_price)
    
    else:
        # Give a message in case of any failure due to restrictions
        print('Ticket booking failed due to restrictions')

if __name__ == "__main__":
    main()