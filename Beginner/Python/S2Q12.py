num = int(raw_input())
num_str = str(num)
rev_str = reversed(num_str)
if list(num_str) == list(rev_str):
   print("palindrome")
else:
   print("not palindrome")
