ids = input("enter your full name: ")
ids = ids.split()
print(ids[::-1])


vowels = "aeiou"
counter = 0
sentence = input("Enter a sentence or word please: ")
for i in sentence:
    if i in vowels:
        counter += 1
print(counter)


for i in range(1, 51):
    if i % 7 == 0:
        print(i)


total = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        total += i
print(total)


names = input("Enter your name: ")
for i in range(1, 4):
    print(names)



for i in range(1, 11):
    print(i * i)


word = "madam"
if word == word[::-1]:
    print("madam is a p")


nums = "123"
total = 0
for i in nums:
    total += int(i)
print(total)


for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i -1:
            print(i)


word = input("Enter a word: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])


list1 = [5, 10, 15, 20]
list2 = [10, 20, 30, 40]
new_list = []
for i in list1 and list2:
    if i in list1 and list2:
        new_list.append(i)
print(new_list)


nums = [100, 50, 80]
numbers = 80
for i in nums:
    if i < numbers:
        numbers = i
print(numbers)

nums = [45, 12, 89, 3, 67, 21]
small_nums = 3
for i in nums:
    if i < small_nums:
        small_nums = i
print(small_nums)




nums = [45, 12, 89, 3, 67, 21]
max_nums = 0
for i in nums:
    if i > max_nums:
        max_nums = i
print(max_nums)




for i in range(1, 10):
    print(i,  "X", 9, "=", 9 * i )


sentence = "the quick brown fox jumps over the lazy dog"
vowels = "aeiou"
counter = 0
for i in sentence:
    if i in vowels:
        counter += 1
print(counter)


nums = [1, 2, 3, 2, 4, 1, 5]
new_nums = []
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
print(new_nums)


lists = [12, 56, 8, 91, 34, 77]
max_nums = 0
for i in lists:
    if i > max_nums:
        max_nums = i
print(max_nums)


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


total = 0
for i in range(1, 51):
    if i % 2 == 0:
        total += i
print(total)


for i in range(1, 11):
    print(i * i)

nums = [1, 2, 3, 4, 5, 6]
new_nums = []
for i in range(len(nums)-1, -1, -1):
    new_nums.append(nums[i])
print(new_nums)

for i in range(11, 1, -1):
    print(i * "*")


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")


for i in range(1, 31):
    if i % 3 == 0:
        print(i)

word = "mountain"
counter = 0
for i in word:
    counter += 1
print(counter)


total = 0
for i in range(1, 11):
    square = i * i
    total += square
print(total)


counter = 0
for i in range(1, 51):
    if i % 2 != 0:
        counter += 1
print(counter)


total = 0
for i in range(1, 101):
    total += i
print(total)


word = "programming"
counter = 0
for i in word:
    if "r" in i:
        counter += 1
print(counter)



for i in range(1, 6):
    print(i, "hello")


nums = [15, 3, 98, 42, 60]
max_nums = 0
for i in nums:
    if i > max_nums:
        max_nums = i
print(max_nums)



total = 1
for i in range(1, 5):
    total *= i
print(total)



for i in range(1, 51):
    if i % 5 == 0:
        print(i)

word = "madam"
if word == word[::-1]:
        print("madam is a p")
else:
    print("madam is not a p")


word = "hello"
vowels = "aeiou"
total = ""
for i in word:
    if i in vowels:
        total += i
print(len(total))


word = "python"
for i in range(len(word) -1, -1, -1):
    print(word[i])


total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)


lists = [10, 20, 30, 40]
total = 0
for i in lists:
    total += i
print(total)



for i in range(1, 11):
    print(i, "X", 5, "=",  5 * i)



name = input("what your full name? ")
result = ""
for i in name:
    if 65 <= ord(i) <= 90:
        result += chr(ord(i) + 32)
    else:
        result += i
print(result)




nums = input("Enter s list of numbers: ").split()
total = 0
for i in nums:
    integer = int(i)
    total += integer
print(total)
average = total / len(nums)
print(average)



word = input("Enter a word: ")
empty_string = ""
for i in word:
    skip = input("please yes for skip the letter enter for not skipping the letter:")
    if skip == "yes":
        print("you skipped the letter")
    else:
        empty_string += i
        print(i)




#while loop
total = 0
while True:
    nums = int(input("Enter a number: "))
    total += nums
    if nums == 0:
        print(total)
        break


#list
nums = [5, 12, 7, 21, 3]
max_nums = 0
for i in nums:
    if i > max_nums:
        max_nums = i
print(max_nums)


#while loop
counter = 0
while counter < 11:
    print(counter)
    counter += 1


word = "python"
for i in range(len(word) -1, -1, -1):
    print(word[i])


lists = ["apple", "bread", "milk", "eggs", "cheese"]
for i in lists:
    if "milk" in i:
        print("found milk")



word = "Abracadabra"
counter = 0
for i in word:
    if i == "a" or i == "A":
        counter += 1
print(counter)


nums = [10, 4, 8, 15, 2]
total = 0
for i in nums:
    total += i
print(total)



nums = [6, 13, 8, 22, 15, 33]
max_nums = 0
for i in nums:
    if i % 2 == 0 and  i > max_nums:
        max_nums = i
print(max_nums)



nums = [7, -3, 0, 11, -1, 5]
counter = 0
for i in nums:
    if i > 0:
        counter += 1
        print(i)
print(counter)


#with for loop
words = ["cat", "apple", "programming", "python", "fun"]
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print(longest)

#and without for loop
words = ["cat", "apple", "programming", "python", "fun"]
longest = ""
if len(words) > len(longest):
    longest = words
    print(longest)



nums = [3, 8, 1, 5, 10]
new_nums = []
for i in nums:
    new_nums.append(i + i)
print(new_nums)


names = ["John", "Mery", "James", "Emily", "Sarah"]
new_names = []
names_starts = "J"
for i in names:
    if names_starts in i:
        new_names.append(i)
print(new_names)


nums = [4, 7, 10, 13, 25]
primes = []
for i in nums:
    if i > 1:
        divisors = 0
        for j in range(2, i):
            if i % j == 0:
                divisors += 1

        if divisors == 0:
            primes.append(i)
print(primes)



nums = [5, 12, 7, 21, 3]
new_nums = []
for i in range(len(nums) -1, -1, -1):
    new_nums.append(nums[i])
print(new_nums)


nums = [3, 9, 10, 12, 15]
new_nums = []
for i in nums:
    if i % 3 == 0:
        new_nums.append(i)
print(new_nums)


nums = [7, 14, 2, 9, 11]
new_nums = []
counter = 0
for i in nums:
    if i % 2 != 0:
        new_nums.append(i)
        counter += 1
print(new_nums)


words = ["pen", "forest", "key", "computer", "table"]
new_words = []
for i in words:
    if len(i) > 4:
        new_words.append(i)
print(new_words)


for i in range(1, 21):
    extra_number = 13
    if i != extra_number:
        print(i)


for i in range(1, 6):
    print(i * "*")


for i in range(1, 21):
    if i % 2 != 0:
        print(i)


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)




for i in range(10, 0, -1):
    print(i)

for i in range(20, 0, -1):
    if i % 2 == 0:
        print(i)


total = 0
for i in range(1, 51):
    total += i
print(total)


for i in range(1, 11):
    if i % 2 == 0:
        print("number", i, "is even")

    elif i % 2 != 0:
        print("number", i, "is odd")


for i in range(1, 11):
    print(7, "*", i, "=", 7 * i)





















