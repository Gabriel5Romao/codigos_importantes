## Hierarquia

Em emmet, para descer na hierarquia você deve inserir um sinal de ">". Pra subir você deve utilizar o sinal de "^". O uso de parênteses é permitido e é bem vindo. Para cada sinal de alteração na hierarquia corresponde a um degrau nela.

Se você quiser adicionar algum outro elementos na hierarquia, coloque utilize o sinal de "+". ` div>ul>li+input^p ` gera o código:

```html
<div>
    <ul>
        <li></li>
        <input type="text">
    </ul>
    <p></p>
</div>
```
##IDs, Class e atributos
Na mesma sintaxe do CSS, você insere "#" e "." após o nome da tag. Pra inserir uma tributo, você utiliza da mesma sintaxe do HTML, dessa vez colocando entre colchetes. O código `input[type="text"]` gera: `<input type="text">`

## Criando vários do mesmo elemento

Você pode usar o sinal de "*" para multiplicar o mesmo elemento. Muito útil para li's. O código ` ul>li*3 ` gera:

```html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

Também é possível utilizar números que se iteram. Se você deseja alterar o ID de uma tag, use o símbolo "$" ( use mais dele para um número maior ). Use ele acompanhado de uma multiplicação, automaticamente ele irá se iterar. O código `ul>li#item$*3` gera:

```html
<ul>
    <li id="item1"></li>
    <li id="item2"></li>
    <li id="item3"></li>
</ul>

```

## Texto e Lorem

Dentro do EMMET você já pode inserir o texto que deseja e ganhar tempo. Para isso, você deve inserir o texto dentro de "{}". Muito útil para texto rápidos. O código `a[href="pudim.com.br"]{Site do Pudim}` gera : `<a href="pudim.com.br">Site do pudim</a>`

Pra gerar um texto Lorem, você o utiliza como nome de tag no Emmet. Por padrão, gera um texto de 30 palavras, mas você pode colocar um número na frente para chegar mais palavras. O código ` lorem100` gera uma tag lorem com 100 palavras.

## Matemática

Você pode fazer cálculos direto do vscode. Após digitar uma conta matemática, você utiliza as teclas "Shift + Ctrl + y" para calcular a expressão.