# program to calculate the sum of all even numbers from 1 to n
n = int(input("Enter a number: "))
# Initialize the sum
sum_even = 0
# Loop through numbers from 1 to n
for i in range(1, n + 1):
    # Check if the number is even
    if i % 2 == 0:
        sum_even += i  # Add to the sum if even