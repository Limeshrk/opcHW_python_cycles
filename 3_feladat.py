x = ['', 4, True]

def type_list(examlist):
  a = []
  for i in range(len(examlist)):
    if type(examlist[i]) is int:
      a.append('integer')
    elif type(examlist[i]) is str:
      a.append('string')
    elif type(examlist[i]) is bool:
      a.append('boolean')
  return a

print(type_list(x))