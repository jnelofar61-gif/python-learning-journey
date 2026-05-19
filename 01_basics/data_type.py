lists = ["virtual tacos", "digital pizza", "cyber coffee"]
for i in lists:
    print(i)

from dataclasses import replace

sentence = "python programming is fun"
print(len(sentence))
print(sentence.upper())


radius = 5
area = 3.14 * radius * radius
print(area)


nums = [10, 20, 30, 40, 50]
print(sum(nums))



import math
price = 7.95
rounded_price = math.ceil(price)
print(rounded_price)


restaurant_items = {"Pizza": 12.99, "Burger": 8.55, "Salad": 6.00}
print(f"{restaurant_items["Pizza"]} ")
print(f"{restaurant_items['Burger']} ")
print(f"{restaurant_items['Salad']} ")



nums1 = 10
nums2 = 5
print(nums1 + nums2)
print(nums1 - nums2)
print(nums1 * nums2)
print(nums1 / nums2)

import random
nums1 = random.randint(1, 10)
nums2 = random.randint(1, 10)
if nums1 > nums2:
    print(nums1)
else:
    print(nums2)



lists = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"{lists[0]}, {lists[4]}")



dic = {"Alice": [85, 90, 92], "Bob": [78, 82, 88]}
sum_alice = sum(dic["Alice"])
sum_bob = sum(dic["Bob"])
average_alice = sum_alice / 3
average_bob = sum_bob / 3
print(average_alice, average_bob)





lists = [5, 9.10, "hello", False]
print(lists[2])
print(f"{lists[2]}")



lists = [4, 10, 2, 8]
average = 0
for i in lists:
    if i > 0:
        average = sum(lists) / len(lists)
print(average)



lists = [4, 10, 2, 8]
average = sum(lists) / len(lists)
print(average)


name = "Alix"
print(name[::-1])

name = "alix"
empty_string = ""
for i in name:
   empty_string = i + empty_string
print(empty_string)


sentence = "python is a powerful and a fun language to learn"
sentence = sentence.split()
print(len(sentence))


lists = [1, 4, 7, 10, 13, 16]
new_lists = []
for i in lists:
    if i % 2 == 0:
        new_lists.append(i)
print(new_lists)


sentence = ("The spectacular scenery in the Rockey Mountains is truly breathtaking,"
            "especially when you see it with fresh eyes")
sentence = sentence.split()
for i in sentence:
    if len(i) > 5:
        print(i[::-1])



nums = 10
result = int(nums) + 5
final_text = str(result)
print(final_text)




nums = 10.5
nums = int(nums)
final_nums = str(nums)
print(nums)
print(final_nums)

str1 = False
str2 = True
print(str1 == str2)
print(str1 != str2)



word = "python"
list_of_word = list(word)
reversed_word = (word[::-1])
print(list_of_word)
print(reversed_word)




word = "python"
new_dic = {}
for i, letter in enumerate(word):
    new_dic[letter] = i + 1
print(new_dic)


word = "python"
my_dic = {i: letter for letter, i in enumerate(word)}
print(my_dic)




























