from book import Book
class Usuario:
    _ids_existentes = set()

    def __init__(self, id, nome=""):
        if id in Usuario._ids_existentes and id != 0:
            raise ValueError("ID já existe. Por favor, use um ID único.")
        self.id = id
        self.nome = nome
        self.livros = []
        Usuario._ids_existentes.add(id)

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id
    
    def adiciona_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Livro.")

    def remover_livro(self, livro_id):
        for livro in self.livros:
            if livro.id == livro_id:
                self.livros.remove(livro)
                return True
        return False

    def verifica_livro(self, livro_id):
        for livro in self.livros:
            if livro.id == livro_id:
                return True
        return False
    
    def tem_livro(self):
        return len(self.livros) > 0
    
    def listar_titulos_livros(self):
        return [livro.titulo for livro in self.livros]

    def listar_ids_livros(self):
        return [livro.id for livro in self.livros]