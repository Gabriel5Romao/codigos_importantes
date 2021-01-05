"""
São funções que, em  geral, trabalham com parâmetros que são funções e iteráveis. Em alguns casos é mais útil utilizar laço for. São úteis para manutenção, digitar menos código e torná-lo mais elegante.


"""
L = [ i for i in range(0,11) ] 

# map(função 1 parametro, iterável) -> Você toma uma função de 1 parâmetro e aplica a algum iterável.

def eleva_cubo(n):
	return n**3
	
a = map(eleva_cubo,L) # Isso faz aplicar a função em cada um dos elementos da lista. Retorna um objeto map, então para uma exibição mais amigável você deve converter para um iterável.

#filter(função booleana, iterável) -> A função escolhida deve trabalhar sempre com verdadeiro ou falso. Se ao aplicada, retornar verdadeiro, então o elemento é adicionado a lista; se for falso, ele não irá para a lista.

b = filter(lambda n: n%2 == 0,L) # Separamos os pares da lista

#reduce(função 2 parametros, iterável) -> menos recomendado de se fazer. Você tem uma função com dois parâmetros, que são os dois primeiros elementos da lista, então vc opera com eles e guarda o resultado, esse resultado é operado com o 3° elemento da lista e então o processo é repetido até o fim da lista.

from functools import reduce # reduce saiu das funções embutidas, então está disponível após import

c = reduce(lambda x,y: x - y, L) # retorna um inteiro, que é a diferença acumulada entre os elementos.








