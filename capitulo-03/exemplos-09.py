"""
Percorrendo uma lista
LISTAS é uma estrutura de dados
é identificada pelos colchetes []
os elementos são separados por vírgula (,)
    impostos = ['MEI', 'IRPF']
os elesmentos podem ser de tipos diferentes
    lst = [[1,2,3],"FULANO", 1]

INICIALIZANDO AS LISTAS
lista = []
ou
lista = list()
"""

impostos = ['MEI', 'IRPF', 'SIMPLES', 1, ['XYZ', 2]]

for imposto in impostos:
    print(imposto)
