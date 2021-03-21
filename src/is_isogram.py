def is_isogram(string):
    str = string.lower()
    dict = {}
    for i in range(len(str)):
        
        if str[i] in dict:
            return False
        else:
            dict[str[i]] = str[i]
    return True    

#print (is_isogram('moOse'))    
print (is_isogram('aba'))    
#print (is_isogram('mas'))    
