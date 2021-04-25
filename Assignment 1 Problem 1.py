# Assignment 1 question 1-No which are divisible by 7 and not by 5 in the range of (2000,3200)
for i in range(2000, 3201):
    # 3201 should be written as it doesn't consider the upper bound
    if (i % 7 == 0 and i % 5 != 0):
        # Condition to check whether the no is divisible by 7 and not divisible by 5
        print(i, end=", ")
print("\b")
