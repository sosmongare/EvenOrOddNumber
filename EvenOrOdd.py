# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
# A number is even if division by 2 gives a remainder of 0.
if (num % 2) == 0:
   print("{0} is Even".format(num))
 # If the remainder is 1, it is an odd number.  
else:
   print("{0} is Odd".format(num))