num = raw_input().split()
num1, num2 = num
num1 = int(num1)
num2 = int(num2)
for N in range(num1,num2 + 1):
   if N > 1:
       for _ in range(2,N):
           if (N % _) == 0:
               break
       else:
           print(N)
