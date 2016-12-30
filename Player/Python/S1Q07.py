str = raw_input()
print(''.join([ str[x:x+2][::-1] for x in range(0, len(str), 2) ]))
