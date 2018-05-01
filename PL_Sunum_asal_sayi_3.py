# Python program to check if the input number is prime or not
num=int(input("Enter an integer:"))


# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times" ,num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")



   #count = 0
#while (count < 9):
 #  print 'The count is:', count
  # count = count + 1

#print "Good bye!"