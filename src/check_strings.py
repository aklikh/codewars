'''
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

'''
def is_merge(s, part1, part2):
    in1=0
    in2=0
    
    for i in s:
        if in1 < len(part1) and part1[in1] == i:
            in1 +=1
        elif in2 < len(part2) and part2[in2] == i:
            in2 +=1
        else:
            return False
        
    if in1 == len(part1) and in2 == len(part2):
        return True
    else:
        return False

print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))        