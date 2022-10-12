# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".


#for-in loop that traverses numbers from 1 to 100
for number in range(1,101):
  #Check that number is divisible by both 3 / 5
  if (number%3==0 and number%5==0):
    print("FizzBuzz")

  #Check that number is divisible by 5
  elif(number%5 == 0):
    print("Buzz")

