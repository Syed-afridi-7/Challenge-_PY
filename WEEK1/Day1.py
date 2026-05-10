def rev(str):
    result= ""
    for i in range(len(str)-1,-1,-1):
        result+=str[i]
    return result
print(rev("hello")) 
# Output: olleh 

###--------------------------------------------------------------------------------------------###

def vowels(str):
    ls=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in str:
        if i in ls:
            count+=1
            
    if count==0:
        return "String Has No vowels"
    return count    
    
x=input('String:')        
print(vowels(x))

###--------------------------------------------------------------------------------------------###

def fact(n):
    if n==0 or n==1:
        return 1
    else:   
        return n * fact(n-1)
x=int(input("n:"))     
print(fact(x))

###--------------------------------------------------------------------------------------------###

def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,b+a
        
x=int(input("n:"))
fibo(x)

###--------------------------------------------------------------------------------------------###

def palindrome(n):
    if n < 0:
        return "Not A Palindrome Number"
    
    original = n 
    rev = 0 
    
    for i in range(len(str(n))):
        digit = n % 10
        rev = (rev * 10) + digit
        n = n // 10  
  
    if rev == original:
        return "Is A Palindrome Number"
    else:
        return "Not A Palindrome Number"

x = int(input("n: "))
print(palindrome(x))


