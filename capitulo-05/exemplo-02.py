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


def main():
    # dicionário nome entidade -> atributos
    meta = dict()

    # dicionário identificador -> nome entidade
    keys = dict()

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
                    print("Entidade {} -> {}".format(key, col[0]))


if __name__ == "__main__":
    main()
