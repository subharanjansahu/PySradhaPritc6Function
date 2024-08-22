'''
WRF to print all element in a list and also print in reversely
hint: use list and index as parameters
'''

heroes = ['iron man','sakti man','thor','hulk','dead pull']

def li_show(l,i=0):
  if(i == len(l)):
    return
  print(l[i])
  li_show(l,i=i+1)
  # print(l[i])  #print list in reverse word
li_show(heroes)