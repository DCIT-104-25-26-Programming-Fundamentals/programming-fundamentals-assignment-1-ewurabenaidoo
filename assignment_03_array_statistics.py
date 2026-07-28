# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)

def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def find_minimum(numbers):
    if len(numbers) == 0:
        return None
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

if __name__ == "__main__":
    count = int(input("How many numbers? "))
    
    if count <= 0:
        print("Error: Number count must be a positive integer.")
    else:
        number_list = []
        for index in range(count):
            current_number = float(input(f"Enter number {index + 1}: "))
            number_list.append(current_number)
            
        total_sum = calculate_sum(number_list)
        average_value = calculate_average(number_list)
        maximum_value = find_maximum(number_list)
        minimum_value = find_minimum(number_list)
        
        print("\nResults:")
        print(f"Sum:     {total_sum}")
        print(f"Average: {average_value}")
        print(f"Maximum: {maximum_value}")
        print(f"Minimum: {minimum_value}")