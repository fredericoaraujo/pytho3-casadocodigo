# Definindo funções

def salario_descontando_imposto(salario, imposto=27.5):
    return salario - (salario * (imposto * 0.01))

salario = int(input("Salário: "))
imposto = float(input("Imposto: "))

print("Valor real: {0}".format(salario_descontando_imposto(salario, imposto)))
