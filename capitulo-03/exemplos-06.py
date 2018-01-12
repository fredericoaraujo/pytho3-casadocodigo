"""
OPERADORES LÓGICOS

Os operadores and e or funcionam como curto circuito
no caso do and (E) caso a primeira expressão seja falsa, não será executada a segunda
no caso do or (OU) caso a primeira expressão seja verdadeira, não será executada a segunda

OPERADORES

and = E
or = OU
not = Negação
"""

imposto = float(input("Imposto: "))

if imposto < 10.:
    print("Baixo")
elif imposto >= 10. and imposto <= 27.:
    print("Médio")
elif imposto > 27. and imposto < 100:
    print("Alto")
else:
    print("Imposto inválido")
