'''WAF to print the length of a list'''

nums = [1,1.6,74,98.34]
heroes = ['iron man','sakti man','thor','hulk','dead pull']

def len_list(li):
  # print('length of the list is',len(li))
  return len(li)

# len_list(nums)
# len_list(heroes)

# return stmt
res1 = len_list(nums)
print("length of nums list is =",res1)
res2 = len_list(heroes)
print("length of heroes list is =",res2)
