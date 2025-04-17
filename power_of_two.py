#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 15, 2025
# Program that gets a whole number from the user.
# It then shows the squared product of every number leading
# up to the user's number.


def main():
    # Get the user's input as a string
    user_input = input("Enter a non-negative integer: ")

    try:
        # Convert the user's input to an integer
        user_num = int(user_input)

        # Check if the user's number is positive (or 0)
        if user_num >= 0:
            # FOR LOOP
            # Starts at 0 and ends at user_num
            for counter in range(user_num + 1):
                # Calculate square product
                product = counter**2
                # Display square product
                # \u00b2 is the unicode for the squared symbol
                print(f"{counter}\u00b2 = {product}")
        else:
            # Tell the user that the number can't be negative
            print(f"Number must be a whole number!")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{user_input} is not an integer.")
    finally:
        # Program completion message
        print("Thanks for Playing!")


if __name__ == "__main__":
    main()
