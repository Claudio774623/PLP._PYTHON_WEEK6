# Week 6 Assignment - Loop Hospital

print("LOOP HOSPITAL")
print("==============")

# Patient 1
# FIXED: range(1, 10) stops before 10, so the stop value was changed to 11.
print("\nPatient 1 - Numbers 1 to 10:")

for i in range(1, 11):
    print(i)


# Patient 2
# FIXED: n must decrease inside the loop so that the while loop eventually stops.
print("\nPatient 2 - Countdown 3 to 1:")

n = 3

while n > 0:
    print(n)
    n = n - 1


# Patient 3
# FIXED: total must be initialized before the loop so that each number is added to the same total.
print("\nPatient 3 - Sum of 1 to 5:")

total = 0

for i in range(1, 6):
    total = total + i

print(total)