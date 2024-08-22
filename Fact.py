'''WAF to find the factorial of n'''

def fact(n):
  fact = 1
  # for loop
  for i in range(1,n+1):
    fact = fact*i
  print(fact)
  # while loop
  # i = 1 
  # while(i<=n):
  #   fact = fact*i
  #   i+=1
  # print(fact)

fact(3)
fact(5)
