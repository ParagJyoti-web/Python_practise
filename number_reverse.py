def reverse_number(num):
    rev = 0
    is_negative = num < 0
    num = abs(num)
    
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
        
    return -rev if is_negative else rev

print(reverse_number(6789)) 