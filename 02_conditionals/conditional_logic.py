#larg number
nums1 = int(input("Enter the first number: "))
nums2 = int(input("Enter the second number: "))
nums3 = int(input("Enter the third number: "))
if nums1 >= nums2 and nums1 >= nums3:
    print(nums1, "is the largest number")
elif nums2 >= nums1 and nums2 >= nums3:
    print(nums2, "is the largest number")
else:
    print(nums3, "is the largest number")



#letter
vowels = "aeiou"
sentence = input("Please enter a letter: ")
if sentence  in vowels:
    print("this letter has vowels")
else:
    print("this letter has no vowels")



#month of years
months = int(input("please enter a number: "))
if months == 1:
    print(months, ": is January which is 31 day ")
elif months == 2:
    print(months, ": is February which is 29 day ")
elif months == 3:
    print(months, ": is March which is 31 day ")
elif months == 4:
    print(months, ": is April which is 31 day ")
elif months == 5:
    print(months, ": is May which is 31 day ")
elif months == 6:
    print(months, ": is June which is 30 day ")
elif months == 7:
    print(months, ": is July which is 31 day ")
elif months == 8:
    print(months, ": is August which is 31 day ")
elif months == 9:
    print(months, ": is September which is 31 day ")
elif months == 10:
    print(months, ": is October which is 31 day ")
elif months == 11:
    print(months, ": is November which is 31 day ")
elif months == 12:
    print(months, ": is December which is 31 day ")
else:
    print("invalid entry!")






#ticket
ticket = int(input("Enter your age? "))
if ticket <= 12:
    print("your price is: $5 ")
elif 12 >=  ticket <= 64:
    print("your price is: $10 ")
else:
    print("your price is: $7 ")



#password
password = "secret123"
user1 = input("Enter your password: ")
if user1 != password:
    print("wrong password")
user2 = input("wrong password, Try again")
if user2 != password:
    print("wrong password")
user3 = input("wrong password, Try your last time!")
if user3 != password:
    print("you failed")
else:
    print("you succeeded")




#sentence
sentence = "Hello everyone welcome to the coding session"
word = "Hello"
if word in sentence:
    print("word founded")
else:
    print("word not found")




#triagular
length1 = int(input("Enter the first length: "))
length2 = int(input("Enter the second length: "))
length3 = int(input("Enter the third length: "))
if length1 == length2 and length2 == length3:
    print("equilateral triangle")
elif length1 == length2 and length2 != length3:
    print("isosceles triangle")
elif length1 != length2 and length2 == length3:
    print("isosceles triangle")
else:
    print("scalene triangle")



#age
age = int(input("Enter your age: "))
if age <= 12:
    print("you are child")
elif age <= 17:
    print("you are teenager")
elif age >= 18 or age <= 65:
    print("you are an adult")
else:
    print("you are senior ")




#card
card = input("Enter one the following options:"
             "1- checking the balance"
             "2- withdrawing the money"
             "3- depositing money")
current_balance = 1000
if card == "2":
    withdrawing = int(input("Enter the amount to withdraw: "))
    result_money = current_balance - withdrawing
    print(result_money)
elif card == "1":
    print("Balance is:", current_balance)

elif card == "3":
    depositing = int(input("Enter the amount to deposit: "))

    print(current_balance + depositing)
else:
    print("invalid entry!")





#grade
#A= 90, 100
#B= 80, 89
#C= 70, 79
#F= 0, 69
grade = int(input("Enter a score: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")





#comparing numbers
nums1 = int(input("Enter the first number: "))
nums2 = int(input("Enter the second number: "))
nums3 = int(input("Enter the third number: "))
if nums1 >= nums2 and nums1 >= nums3:
    print(nums1, "is larger number")
elif nums2 >= nums1 and nums2 >= nums3:
    print(nums2, "is larger number")
else:
    print(nums3, "is larger number")


if nums1 <= nums2 and nums1 <= nums3:
    print(nums1, "is smaller number")
elif nums2 <= nums1 and nums2 <= nums3:
    print(nums2, "is smaller number")
else:
    print(nums3, "is smaller number")


if nums1 == nums2 or nums1 == nums3 or nums2 == nums3:
    if nums1 == nums2 and nums2 == nums3:
        print(nums1, nums2, nums3, "are equal")
    else:
        print(nums1, nums2, nums3, "are equal")
else:
    print("all numbers are different")





#identifying numbers
nums = int(input("Enter a number: "))
if nums == 0:
    print(nums, "zero")
elif nums < 0:
    print(nums, "negative number")
elif nums > 0:
    print(nums, "positive number")
elif nums == 100:
    print(nums, "that is perfect century")
else:
    print("invalid ")









#Operation with numbers
nums1 = int(input("Enter a first number: "))
nums2 = int(input("Enter a second number: "))
operation = input("Enter the right operation: +, -, *, /: ")

if operation == "+":
    print(nums1 + nums2)
elif operation == "-":
    print(nums1 - nums2)
elif operation == "*":
    print(nums1 * nums2)
elif operation == "/":
    print(nums1 / nums2)
else:
    print("invalid input")



