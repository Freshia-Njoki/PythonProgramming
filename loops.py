# while loop
number = 20
while number <= 25:
    print(number)
    number += 1

# Decrementing values
a = 10
while a >= 1:
    print(a)
    a -= 1

# For loop
languages = ["python", "PHP", "Kotlin", "C++"]
print(languages)
for x in languages:
    print(x)

# Range - by default starting point is from 0, end is -1
for x in range(10):
    print(x)

for b in range(15, 20):
    print(b)

# with incremental
for c in range(4, 30, 2):  # (starting point, ending point, incremental by val)
    print(c)
