# #task 1.1
# numbers=[4,8,15,16,23,42]
# for num in numbers:
#     print(num, end=' ')
# #task 1.2
# numbers=[4,8,15,16,23,42]
# for num in numbers:
#     print(num)
# #task 1.3
# try:
#     numbers = int(input("Enter your number:"))
#     number2 = numbers + 1
#     number3 = numbers + 2
#     print(numbers)
#     print(number2)
#     print(number3)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# #task 1.4
# numbers = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
# total = numbers + number2 + number3
# print(total)
# #task 1.5
# edge = int(input("enter the edge sum"))
# volume = edge ** 3
# surface = 6 * (edge ** 2)
# print(volume)
# print(surface)
# #task 2.1
# children = int(input("Enter the number of child:"))
# apple = int(input("Enter the number of apple"))
# apple_per_student = apple // children
# apple_remaining = apple % children
# print(apple_per_student)
# print(apple_remaining)
#task 2.2
# number = int(input("Enter:"))
# if 1000 <= number <= 9999:
#     thousands = number // 1000
#     hundreds = (number // 100) % 10
#     tens = (number // 10) % 10
#     units = number % 10
#
#     print(f"The digit in the thousands position is {thousands}")
#     print(f"The digit in the hundreds position is {hundreds}")
#     print(f"The digit in the tens position is {tens}")
#     print(f"The digit in the units position is {units}")
# else:
#     print("Please enter a valid four-digit number.")

# #task 2.3
# people = int(input("The population number: "))
# if people % 2 == 0:
#      half = people // 2
# else:
#      half = (people + 1) // 2
# print(half)

# # Task 2.4
# NUM1 = int(input("Enter a number: "))
# Result = NUM1 << 1
# if Result == 0:
#      print("The result of << is zero. Please enter a different number.")
# else:
#      print("The result of << is", Result)

# #Task 2.5
# try:
#     num1 = float(input("Please enter the first number: "))
#     num2 = float(input("Please enter the second number: "))
#     operation = input("Please choose the operation (+, -, *, /): ")

#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             raise ZeroDivisionError("Division by zero is not allowed.")
#     else:
#         raise ValueError("Invalid operation entered.")

#     print(f"{num1} {operation} {num2} = {result:.3f}")

# except ValueError as ve:
#     print(f"Error: {ve}")
# except ZeroDivisionError as zde:
#     print(f"Error: {zde}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")