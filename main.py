# Eric Reece - 1/3/2021
# This is a sample program whose function is to determine whether a user's input is a prime number or not.


# Function to calculate the math required, given user value
def prime_test(value):
    if value > 1:
        for i in range(2, value):
            if (value % i) == 0:
                print(value, " is not a prime number.")
                print(i, "times", value // i, "is", value)
                break
        else:
            print(value, " is a prime number.")
    else:
        print(value, " is not a prime number.")


if __name__ == '__main__':
    print("This program determines whether a number is a prime or not.\nPrime numbers are whole numbers "
          "greater than 1, that have only two factors – 1 and the number itself."
          "\nPrime numbers are divisible only by the number 1 or itself.  ")
    test_again = True

    while test_again:
        try:
            user_number = int(input("Please enter a number to be tested.\nTesting: "))
            prime_test(user_number)
        except ValueError:
            print("Please enter integers only.")

        user_choice = input("Test another value? (y/n):\n")
        if user_choice == 'y':
            test_again = True
        elif user_choice == 'n':
            test_again = False
            print("Good bye.")
        else:
            print("Please enter either yes (y) or no (n)")

