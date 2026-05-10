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

