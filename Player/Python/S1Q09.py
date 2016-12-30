lower,upper = raw_input().split()
lower = int(lower)
upper = int(upper)

count = 0
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           count +=1
print(count)
