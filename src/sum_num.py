'''Description:

Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!'''





def get_sum(a,b):
    if a == b:
        return a
    if a > b:
        start = b
        stop = a
    else:
        start = a
        stop = b
        
   
    answ = start
    while start < stop:
        start +=1
        answ += start
      
    
    return answ

print(get_sum(-4,9))        