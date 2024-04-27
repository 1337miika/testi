# Random number generator

import random

def roll ():
    min_value=1
    max_value=9999
    roll = random.randint(min_value, max_value)

    return roll



print ("Do you want to double the number? yes/no")

# Defines

def generate_random_number():
    """
    Generate a random number between 1 and 100.
    
    Returns:
        int: Random number generated.
    """
    min_value = 1
    max_value = 9999
    result = random.randint(min_value, max_value)
    return result

def double_value(number):
    """
    Double the given number.
    
    Args:
        number (int): Number to double.
    
    Returns:
        int: Doubled value.
    """
    return number * 2

# Generate a random number
value = generate_random_number()

# Print the random number generated
print("Random number is here:", value)

# Ask user if they want to double the value
choice = input("Do you want to double the value? (yes/no): ")

# Check user's choice and double the value if requested
if choice.lower() == "yes":
    doubled_value = double_value(value)
    print("Doubled value:", doubled_value)
else:
    print("Okay, no doubling.")