# Question 5: List Analysis

numbers = []

print("Enter 5 numbers:")
for _ in range(5):
    num = float(input())
    numbers.append(num)

print("Numbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Sorted:", sorted(numbers))
