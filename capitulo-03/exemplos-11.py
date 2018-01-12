# packing e uńpacking

from datetime import date


d = (2013, 3, 15)

print("\n==== Tuplas ====")
# quando for tuple (tupla) é necessário utilizar 1 asterisco (*) na frente da variavel
print(date(*d))

# outro exemplo usando tuplas
print("\n==== Outro exemplo com tuplas ====")
def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]

    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1, 2, 3, 4, 5, 6)

print("\n==== Dicionários ====")

def new_user(active=False, admin=False):
    print("active: ", active)
    print("admin: ", admin)

config = {"active": False, "admin": True}

# quando for dict (dicionário) é necessário utilizar 2 asteriscos (**) na frente da variavel
new_user(**config)


def unpacking_experiment(**kwargs):
    print(kwargs)

print("\n==== Outro exemplo com dicionário ====")
unpacking_experiment(named="Test", other="Other")
