'''The following program calculates a discount depending on the day of the week.'''


import datetime

def main():
    # Get the current date and time
    current_date_and_time = datetime.datetime.now()

    # Call the weekday() method to get the day of the week from the current_date_and_time object.
    day_of_week = current_date_and_time.weekday()

    #0 = Monday
    #1 = Tuesday
    #2 = Wednesday
    #3 = Thursday
    #4 = Friday
    #5 = Saturday
    #6 = Sunday

    # Assuming the conditions for discount apply to Tuesday (1) and Wednesday (2)
    discount_days = [1, 2]

    # Asking directly for the subtotal
    subtotal = float(input("Please enter the subtotal: "))

    # Initialize the discount variable
    discount = 0

    # Apply discount if the conditions are met (it's Tuesday or Wednesday and subtotal >= 50)
    if subtotal >= 50 and day_of_week in discount_days:
        discount = subtotal * 0.10  # 10% discount
        subtotal -= discount
    elif day_of_week in discount_days and subtotal < 50:
        # If it's Tuesday or Wednesday and not enough to receive a discount
        additional_needed = 50 - subtotal
        print(f"Add ${additional_needed:.2f} more to qualify for a 10% discount.")

    # Calculate the sales tax and the total amount
    sales_tax = subtotal * 0.06
    total_due = subtotal + sales_tax

    # Output results
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total_due:.2f}")

if __name__ == "__main__":
    main()