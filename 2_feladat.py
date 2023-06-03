players = ['Peter', 'Kate', 'John']

def index_listazo(lista):
  for i in range(len(lista)):
    index = i + 1
    print(f'{index}. {lista[i]}')

#TEST
index_listazo(players)