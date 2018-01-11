txt1 = "Olá, mundo!"
txt2 = 'Olá, mundo!'

# Aqui o caracter barra '\' faz o esape da quebra de linha '\n'
txt3 =  """\
Olá,
Mundo!
"""

print("Aspas duplas")
print(txt1)
print("\nAspas simples")
print(txt2)
print("\nMulti-linha")
print(txt3)


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

