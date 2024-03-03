import random

print(random.randint(5, 20))  
# line 1          
#output：19      
#In row 1, the smallest number is 5 and the largest number is 20.

print(random.randrange(3, 10, 2))  
# line 2     
#output：3       
#In row 2, the smallest number is 3 and the largest number is 9. Line 2 does not produce 4 because the step size is 2, so it does not produce an even number.

print(random.uniform(2.5, 5.5))  
# line 3       
#output：4.016736854985234
#In row 3, the smallest number is 2.5 and the largest number is 5.5.

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))