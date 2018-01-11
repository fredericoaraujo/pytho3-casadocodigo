# Capítulo 2

## Textos

Em Python temos somente o tipo _string_ para cadeia de caracteres, o seu tamanho varia de 0 (zero) até o tamanho máximo suportado.
A partir da versão 3.3 do Python todas as strings são unicodes, anteriormente elas começavam com u"Uma string" para identificar como unicode.

Para criar uma string temos que envolvê-las em aspas simples ('string') ou duplas ("string"). Para multi-linhas precisamos de iniciar e finalizar com 3 aspas, como no exemplo abaixo:
```python
"""
Aqui temos um texto
multi-linha
"""
```

#### Algumas dicas como manipular strings em python:

```python
# Manipulando Strings
print("\n===== Manipulando Strings ====")
str = 'PYTHON'
print("String: ", str)

print("\nInvertendo a string")
print("str[::-1] => ", str[::-1])

print("\nTamanho da string")
print("len(str) => ", len(str))

print("\nAcesso por índice da string")
print("str[0] => ", str[0])

print("\nTrechos (slice)")
print("str[1:2] => ", str[1:2])
print("str[:2] => ", str[:2])

print("\nContem/Não contem string")
print("('Y' in str) => ", ("Y" in str))
print("('X' in str) => ", ('X' in str))

print("\nConcatenação da string")
print("str + ' 3' => ", (str + ' 3'))
```

### Strings são imutáveis

Você não consiguirá alterar de maneira simples uma string em Python, para isso você terá que utilizar algum método para fazê-lo.

```python
str = 'PYTHON'
str[1] = 'I'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

```python
str = 'PYTHON'
str.replace('Y', 'I')

# OU

str = 'PYTHON'
str[:-1] + "M"
```
### Principais métodos da classe String

* Capitlize
    * Transforma a primeira letra da _string_ em maiúscula
    * str.capitalize()

* Count
    * Conta a quantidade de vezes que repete um determinado caracter
    * Retorna um inteiro
    * str.count('a')

* Starts With
    * Verifica se uma _string_ inicia com um determinado caracter
    * Retorna um booleano
    * str.startswith('a')

* Ends With
    * Verifica se uma _string_ finaliza com um determinado caracter
    * Retorna um booleano
    * str.endswith('a')

* Split
    * Quebra uma string por determinado caracter
    * Quando não se passa parametro, vai ser quebrado pelo espaço entre as palavras
    * str.split()

* Join
    * Junta as palavras de uma lista
    * ' '.join(['Chico', 'Anísio'])

### Interpolação de Textos


Há basicamente duas maneiras de se interpolar textos, utilizando o sinal de porcentagem (%) e as chaves ({}), sendo o segundo o mais utilizado ultimamente por não haver necessidade de saber o tipo do dado.

```python
"%d dias para copa" % (100)
"{} dias para copa".format(100)
"{dias} dias para copa".format(dias=100)
```
