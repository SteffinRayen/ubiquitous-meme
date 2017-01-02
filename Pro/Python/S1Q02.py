numStr = raw_input().split()
num,k = numStr
k = int(k)
intList = [int(i) for i in str(num)]
intList.sort()
l=len(intList)
newIntList = intList[:l-k]
print(int(''.join(map(str,newIntList))))
