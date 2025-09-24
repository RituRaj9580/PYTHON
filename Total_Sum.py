# Initialize the sum to 0
total_sum = 0
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
# Set the range from input values
# Use a for loop to iterate from a to b (inclusive)
for number in range(a,b+1):
    total_sum += number

# Display the final sum
print(f"The sum of integers from {a} to {b} is:", total_sum)
