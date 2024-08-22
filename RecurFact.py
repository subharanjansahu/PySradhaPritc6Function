def fact(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * fact(n-1)
  
res = fact(5)
print(res)

'''
n! = n * (n-1)!
'''