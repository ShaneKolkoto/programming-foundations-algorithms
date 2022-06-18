# Find the greatest common denominnator of teo numbers
# Using Euclid's algorith

def gcd(num1, num2):
    while (num2 != 0): # 0 should be he reminder
        t = num1 # Store a in a tempory variable
        num1 = num2 # If Reminder not 0 b gets stored in a
        num2 = t % num2
    return num1

# try out the function with a few examples
print(gcd(60, 96))  # Should be 12
print(gcd(20, 8))   # Should be 4