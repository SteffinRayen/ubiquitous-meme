num = int(raw_input())
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("non prime")
           break
   else:
       print("prime")
else:
   print("non prime")
