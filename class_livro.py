class Livro:
    _ids_existentes = set()

    def __init__(self, titulo, id, em_estoque=True):
        if id in Livro._ids_existentes and id != 0:
            raise ValueError("ID já existe. Por favor, use um ID único.")
        self.titulo = titulo
        self.id = id
        self.em_estoque = em_estoque
        Livro._ids_existentes.add(id)
