'''WAF to print the elements of a list in a single line'''
heroes = ['iron man','sakti man','thor','hulk','dead pull']

# for i in heroes:
#   print(i)

def sing_list(li):
  for i in li:
    print(i,end=",")

sing_list(heroes)