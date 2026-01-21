# # 1. Print squares of numbers from 1 to 10
# for i in range(1, 11):
#     print(i * i)

# 2. Iterate through a string and count vowels
# text = "Education"
# vowels = "aeiouAEIOU"
# count = 0

# for char in text:
#     if char in vowels:
#         count = count + 1

# print("Total vowels:", count)


# 3. Given a list of marks, print only the marks greater than 50 using a for loop.
# marks = [45, 78, 90, 33, 55, 60]

# for mark in marks:
#     if mark > 50:
#         print(mark)

# 4. WAP to print multiplication table of a number entered by the user
# num = int(input("Enter a number for the table: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 5. WAP using while loop to print all odd numbers between 1 and 20.
# i = 1
# while i <= 20:
#     print(i)
#     i += 2  # Increment by 2 to skip even numbers

# 6. WAP to repeatedly ask for a password until the user enters the correct one.
# correct_pass = "arhamkhan"

# while True:
#     guess = input("Enter password: ")
#     if guess == correct_pass:
#         print("Access Granted")
#         break  
#     else:
#         print("Try again")

# 7. Keep taking input from the user until they type “stop”.
# while True:
#     user_input = input("Type something (or 'stop' to exit): ")
#     if user_input == "stop":
#         print("Exiting...")
#         break
#     print("You typed:", user_input)



# 8. Calculate the sum of numbers from 1 to n.
# n = int(input("Enter a number (n): "))
# total_sum = 0

# for i in range(1, n + 1):
#     total_sum = total_sum + i

# print("The sum is:", total_sum)

# 9. Find the largest number in a list without using max().
# numbers = [12, 45, 2, 99, 54, 8]
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("The largest number is:", largest)

# 10. Print all elements of a list using a for loop.
# items = ["ARHAM", "AYLA", "GULALAY", "MARYAM"]

# for item in items:
#     print(item)

# 11. Keep reading numbers until the user enters a negative number; then print the average
# total = 0
# count = 0

# while True:
#     num = int(input("Enter a number (negative to stop): "))
    
#     if num < 0:
#         break
    
#     total = total + num
#     count = count + 1

# if count > 0:
#     print("Average:", total / count)
# else:
#     print("No positive numbers were entered.")

# 12. Check if a number is a palindrome using a while loop.
num = int(input("Enter a number to check: "))
temp = num
reverse_num = 0

while temp > 0:
    digit = temp % 10            
    reverse_num = (reverse_num * 10) + digit
    temp = temp // 10            

if num == reverse_num:
    print("It is a palindrome.")
else:
    print("It is NOT a palindrome.")







