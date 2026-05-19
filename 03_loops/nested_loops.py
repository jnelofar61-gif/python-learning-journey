for i in range(1, 6):
    for j in range(1, 11):
        print(i,"X",  j,  "=", i * j)


for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i:2} * {j:2}  = {i * j:<10} --- ", end=" ")
    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    print( i * "a")



for i in range(6, 1, -1):
    for j in range(1, i - 1):
        print(j, end=" ")
    print()



n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print(" * ", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print(" * ", end=" ")
    print()


n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print(i, end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print(i, end=" ")
    print()



n = 10

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print(f"{i:<2}", end="  ")
    print()


for i in range(1, 11):
    for j in range(1, i + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


