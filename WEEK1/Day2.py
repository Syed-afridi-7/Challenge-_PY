def isanagram(s, t):

    if len(s) != len(t):
        return False
        
    d = {}
    
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            
    for j in t:
        if j not in d:
            return False
        else:
            d[j] -= 1     
            if d[j] < 0: 
                return False
                
    for count in d.values():
        if count != 0:
            return False
            
    return True

print(isanagram("silent", "listen")) # True
print(isanagram("rat", "car"))       # False

####------------------------------------------------------------------------------------------------------------###

def is_armstrong_math(n):
    if n < 0:
        return False
    
    original = n
    num_digits = len(str(n)) 
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit ** num_digits
        n //= 10
    
    return total == original

####------------------------------------------------------------------------------------------------------------###

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    
    return second if second != float('-inf') else None
