





nums = int(input("enter a number? "))
result = 1
while nums > 0:
    result = result * nums
    nums -= 1
    print(result)



name = input("Enter your name: ")
counter = 0
while counter <= 2:
    counter += 1
    print(name)


text = input("Enter a sentence or a word? ")
index = 0
while index < len(text):
    print(text[index])
    index += 1



sentence = input("Enter a sentence or a word? ")
for i in sentence:
    print(i)



total = 0
while True:
    nums = int(input("Enter a number: "))
    if nums == 0:
        break
    elif nums != 0:
        total += nums
print(total)


total = 0
while True:
    nums = int(input("Enter a number: "))
    if nums == 0:
        break
    elif nums != 0:
        total += nums
print(total)


empty_list = []
while True:
    names = input("Enter a name please: or enter stop ")
    if names == "stop":
        break
    else:
        empty_list.append(names)
print(empty_list)



while True:
    word = input("Enter a word: ")
    print(word[::-1])
    break


total = 0
counter = 1
while counter <= 20:
    total += counter
    counter += 1
print(total)


total = 0
for i in range(1, 21):
    total += i
print(total)




counter = 0
while counter < 10:
    counter += 1
    print(8, "*", counter, "=", 8 * counter)


while True:
    number = int(input("Enter your age: "))
    if number <= 18:
        print("your young")
    elif number > 18:
        print("you are an adult")
    elif number == 0:
        print("invalid input!")
        break
    stop = input("would you like to stop? y/n: ")
    if stop == "n":
        continue
    elif stop == "y":
        break



counter = 0
while counter <= 9:
    counter += 1
    print(7, "*", counter, "=", 7 * counter)



i = 10
while i >= 0:
    print(i)
    i -= 1
print("blass of")




total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)



total = 0
while True:
    for i in range(1, 11):
        total += i
    print(total)
    break


counter = 1
while counter <= 4:
    counter += 1
    square = counter * counter
    print(square)



counter = 1
while counter < 31:
    counter += 1
    if counter % 3 == 0:
        print(counter)


while True:
    nums = int(input("Enter a number: "))
    if nums == 0:
        break

