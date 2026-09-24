# Week 6 Assignment - Times Table

number = int(input("Enter a number: "))

print(f"\nTimes table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
    
    Enter a number: 7

Times table for 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

7 x 10 = 70