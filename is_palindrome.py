def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    
    original = num
    rev = 0
    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        
    return rev == original


print(is_palindrome(121)) 
print(is_palindrome(123))  
print(is_palindrome(-121)) 
print(is_palindrome(101))
print(is_palindrome(102))