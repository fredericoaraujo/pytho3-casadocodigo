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
