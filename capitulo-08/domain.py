from decimal import Decimal

class DataTable:
    """
    Representa uma tabela de dados.

    Essa classe representa uma tabela de dados do portal
    da transparência. Deve ser capaz de validar linhas
    inseridas de acordo com as colunas que possui. As
    linhas inseridas ficam registradas dfentro dela.

    Attributes:
        name: Nome da tabela
        columns: [Lista de colunas]
        data: [Lista de dados]
    """

    def __init__(self, name):
        """
        Construtor

        Args:
            name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self._references =[]
        self._referenced = []
        self._data = []


    def add_column(self, name, kind, description=None):
        self._validate_kind(kind)
        column = Column(name, kind, description)
        self._columns.append(column)
        return column


    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")


    def add_references(self, name, to, on):
        """
        Cria uma referencia dessa tabela para um outra tabela

        Args:
            name: nome da relação
            to: instância da tabela apontada

            on: instância coluna em que existe a relação
        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)


    def add_references(self, name, by, on):
        """
        Cria uma referência para outra tabela que aponta para essa.

        Args:
            name: nome da relação
            by: instância da tabela que aponta para essa
            on: instância coluna em que existe a relação
        """

        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)


class Column:
    """
    Representa um coluna em um DataTable

    Essa classe contém as informações de uma coluna
    e deve validar um dado de acordo com o tipo de
    dado configurado no construtor.

    Attributes:
        name: Nome da Coluna
        king: Tipo de dado (varchar, bigintm numeric)
        description: Descrição da coluna
    """

    def __init__(self, name, kind, description=""):
        """
        Construtor

        Args:
            name: Nome da Coluna
            kind: Tipo do dado (varchar, bigint, numeric)
            desciption: Descrição da coluna
        """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False


    @staticmethod
    def validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True


    def __str__(self):
        return "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)


class PrimaryKey(Column):
    def __init__(self, name, kind, description=""):
        super().__init__(name, kind, description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)

        return "{} - {}".format('PK', _str)


class Relationship:
    """
    Classe que representa um relacionamento entre DataTables

    Essa classe tem todas as informações que identificam um
    relacionamento entre tabelas. Em qual coluna ele existe,
    de onde vem e para onde vai.
    """
    def __init__(self, name, _from, to, on):
        """
        Constructor

        Args:
            name: Nome
            from: Tabela de onde sai
            to: Tabela para onde vai
            on: instância de coluna onde existe
        """
        self._name = name
        self._from = _from
        self._to = to
        self._on = on
