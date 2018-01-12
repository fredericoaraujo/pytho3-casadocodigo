"""
if <condicao>:
    faca_alguama_coisa
elif <condicao>: # funciona como senão se
    faca_outra_coisa
else:
    faca_o_padrao
"""

imposto = float(input("Imposto: "))
if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito alto")
