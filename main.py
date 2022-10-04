
# ******************************
# Make your Code
# ******************************
numbers = []

for i in range(5):
    numbers.append(int(input()))

total = sum(numbers)
total = total - min(numbers) - max(numbers)
