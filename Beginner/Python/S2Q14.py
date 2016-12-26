num = raw_input().split()
num1,num2 = num
num1 = int(num1)
num2 = int(num2)
if (num1%2 == 0):
  for _ in range(num1+1,num2+1,2):
    print (_)
else:
  for _ in range(num1,num2+1,2):
    print (_)
