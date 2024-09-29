a = 3000  # Define the range limit

for num in range(1, a + 1):  # Iterate through numbers from 1 to 3000
    c = 0  # Initialize a counter to count divisors
    rev = 0  # Initialize reverse variable for palindromic check
    temp = num  # Temporary variable to manipulate without affecting the original number

    # Check if the number is prime
    for i in range(1, temp + 1):
        if temp % i == 0:  # Check if 'i' is a divisor of 'temp'
            c += 1  # Increment the counter for each divisor

    # If the number has exactly two divisors, it's prime
    if c == 2:
        # Check if the number is a palindrome
        original_num = temp
        while temp > 0:
            rev = rev * 10 + (temp % 10)  # Calculate the reverse of the number
            temp //= 10  # Remove the last digit from 'temp'

        if rev == original_num:  # Check if the reverse is equal to the original number
            print(original_num)  # Print the number if it’s a palindromic prime
