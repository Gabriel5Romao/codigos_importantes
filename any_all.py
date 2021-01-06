#all(iterável) -> retorna True se todos os elementos do iterável são True, ou se o iterável é vazio

a = all((False,False,False,False,False)) # retorna False
b = all((False,False,False,False,False,True,False,False)) # retorna False

c = [ i for i in range(-1,2) ] 
del c[c.index(0)]
print(all(c)) # Devolve True, pois tiramos o 0 da lista.

#any(iterável) -> retorna True se algum elemento do iterável é True, se o iterável é vazio então retorna False

d = any((False,False,False,False,False,True,False,False)) # retorna True
