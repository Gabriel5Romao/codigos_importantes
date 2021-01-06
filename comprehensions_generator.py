"""
List Comprehensions:
  Maneira rápida e elegante para criação de listas.
  
  1° forma:
    [ elemento_com_operacao for elemento in iterable ]
    
  2° forma:
    [ elemento_com_operacao for elemento in iterable if condicao ]
    
  3° forma:
    [ elemento_com_operacao if condicao else outra_operacao for elemento in iterable ]
  
  Aninhadas:
    [ [ list_comprehension1 ] for x in interable ]
    Na situaçãoa acima o "for x in iterable" é executado primeiro.
"""

algarismos_quadrado = [ i**2 for i in range(0,10)]

pares = [ j for j in range(1,10) if j%2==0 ]
impares = [ m for m in range(1,10) if m%2!=0 ]

lista_louca = [ x ** 2 if x%2==0 else x /2 - 1 for x in range(1,10) ] 
# Se x é par eleva ao quadrado, caso contrário divida por 2 e subtraia 1

"""
Dict Comprehensions:
  Sintaxe:
    { chave:valor for chave,valor in interable }
  
"""

"""
Tuple comprehensions é generators, tem a mesma sintaxe de List comprehension
"""




