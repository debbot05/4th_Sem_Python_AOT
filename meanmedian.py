def calculate_mean(elements):
    return sum(elements) / len(elements)

def calculate_median(elements):
    sorted_elements = sorted(elements)
    n = len(sorted_elements)
    
    if n % 2 == 0:
        # If the number of elements is even, average the middle two
        middle1 = sorted_elements[n // 2 - 1]
        middle2 = sorted_elements[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the number of elements is odd, take the middle element
        median = sorted_elements[n // 2]
    
    return median

# Taking input from the user
user_input = input("Enter elements separated by space: ")
elements = [float(x) for x in user_input.split()]

# Calculating and displaying mean and median
mean = calculate_mean(elements)
median = calculate_median(elements)

print(f"Mean: {mean}")
print(f"Median: {median}")