def binary_to_decimal():
    binary_str = input("Enter a binary number: ")
    decimal_value = 0

    try:
        decimal_value = int(binary_str, 2)
        print("Binary: {} = Decimal: {}".format(binary_str, decimal_value))
    except ValueError:
        print("Invalid binary number entered.")

binary_to_decimal()




def filter_words(input_tuple):
    filtered_tuple = ()
    for word in input_tuple:
        if 'a' in word and 'b' in word and len(word) > 4:
            filtered_tuple += (word,)
    return filtered_tuple



import random

def generate_random_elements(count):
    return [random.randint(1, 100) for _ in range(count)]

def split_and_save_elements(count):
    random_elements = generate_random_elements(count)
    categories = {'even_elements': [], 'odd_elements': [], 'divisible_by_3_elements': []}

    for element in random_elements:
        if element % 2 == 0:
            categories['even_elements'].append(element)
        if element % 2 != 0:
            categories['odd_elements'].append(element)
        if element % 3 == 0:
            categories['divisible_by_3_elements'].append(element)

    for category, elements in categories.items():
        with open(f"{category}.txt", "w") as file:
            file.write("\n".join(map(str, elements)))

split_and_save_elements(50)


def fibonacci_rabbits(months):
    a, b = 0, 1
    for _ in range(months):
        a, b = b, a + b
    return a

def record_fibonacci_results(months, filename):
    with open(filename, "w") as file:
        for month in range(months + 1):
            file.write(f"Month {month}: {fibonacci_rabbits(month)} rabbits\n")

if __name__ == "__main__":
    months = int(input("Enter the number of months: "))
    record_fibonacci_results(months, "fibonacci_results.txt")



import random
import math

def calculate(choice):
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    if choice == 0:
        return f"Generated 0. Multiplying {num1} by {num2} using a loop: {num1 * num2}"
    elif choice == 1:
        return f"Generated 1. Calculating factorial of {num1} using a while loop: {math.factorial(num1)}"
    else:
        return f"Generated 2. Multiplying {num1} by {num2} recursively: {num1 * num2 if num2 == 1 else num1 + calculate(2).split(': ')[-1]}"

def main():
    choice = random.randint(0, 2)
    result = calculate(choice)
    print(result)

if __name__ == "__main__":
    main()






