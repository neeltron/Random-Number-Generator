# This is a random number generator that works on the basis of users' time in seconds and the time taken by the user to input the range in which they want the random number.

import time
from datetime import datetime

now = datetime.now()
cur = now.strftime("%S")
print(cur)

start = time.time()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the last number: "))
stop = time.time()

final = stop - start
final = str(final)
somenum = int(final[4])

if somenum < num1:
  rand = somenum + num1
else:
  rand = num2 - somenum
  rand - int(cur)

print(rand)

# rand = num1 / somenum
# if rand < num2 and rand > num1:
#   print(int(rand))
# else:
#   rand = num2 / somenum
#   print(int(rand))
