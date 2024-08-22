def show(n):
  if(n == 0):   # base case/stoping condition (its the condition to terminate the function)
    return
  print(n)
  show(n-1)
  # print('end')

show(5)