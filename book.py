class Book:
    
    def __init__(self, id, title, author, genre):
        # Verificar se o id já existe no banco
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False

    def register_new_book(self, cursor):
        cursor.execute('''
        INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)''', 
        (self.id, self.title, self.author, self.genre, self.borrowed))