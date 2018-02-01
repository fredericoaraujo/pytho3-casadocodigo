import os

BASE_DIR = 'data/meta-data'


def extract_name(name):
    return name.split('.')[0]


def read_lines(filename):
    _path = os.path.join(BASE_DIR, filename)
    _file = open(_path, 'rt')
    data = _file.read().split('\n')
    _file.close()
    return data


def read_metadata(filename):
    metadata = list()
    for column in read_lines(filename):
        if column:
            values = column.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            # adiciona uma tuple
            metadata.append((nome, tipo, desc))

    return metadata


def prompt():
    print("\nO que deseja ver?")
    print("(l) Listar entidades")
    print("(d) Exibir atributos de uma entidade")
    print("(r) Exibir referências de uma entidade")
    print("(s) Sair do programa")
    return input('')


def main():
    # dicionário nome entidade -> atributos
    meta = {}

    # dicionário identificador -> nome entidade
    keys = {}

    # dicionário de relacionamentos
    relationship = {}

    for meta_data_file in os.listdir(BASE_DIR):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationship[key] = keys[col[0]]

    opcao = prompt()
    while opcao != 's':
        if opcao == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif opcao == 'd':
            entity_name = input('Nome da entidade: ')
            for col in meta[entity_name]:
                print(col)
        elif opcao == 'r':
            entity_name = input('Nome da entidade: ')
            other_entity = relationship[entity_name]
            print(other_entity)
        else:
            print('Inexistente')

        opcao = prompt()


if __name__ == "__main__":
    main()
