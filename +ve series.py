def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print(positive_numbers)

# Example 1
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print("Output:", end=" ")
print_positive_numbers(list1)

# Example 2
list2 = [12, 14, -95, 3]
print("Input:", list2)
print("Output:", end=" ")
print_positive_numbers(list2)
