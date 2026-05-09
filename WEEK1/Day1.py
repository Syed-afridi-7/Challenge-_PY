#Reverse a string without [::-1]:

def rev(str):
    result= ""
    for i in range(len(str)-1,-1,-1):
        result+=str[i]
    return result
print(rev("hello")) 
# Output: olleh 
