def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev == original

def count_palindromes(L, R):
    count = 0
    for i in range(L, R + 1):
        if is_palindrome(i):
            count += 1
    return count

L = int(input("Enter start of range: "))
R = int(input("Enter end of range: "))

print("Number of palindromes in range:", count_palindromes(L, R))# Function to check if a number is a palindrome