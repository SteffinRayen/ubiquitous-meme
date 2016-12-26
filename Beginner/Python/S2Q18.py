num = raw_input().split()
num1, num2 = num
num1 = int(num1)
num2 = int(num2)
for N in range(num1,num2 + 1):
   order = len(str(N))
   sum = 0
   temp = N
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if N == sum:
       print(N)
