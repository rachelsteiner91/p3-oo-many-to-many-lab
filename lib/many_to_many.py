class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    #This method should return a list of related contracts.
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    #This method should return a list of related books using the Contract class as an intermediary
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    #This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
    
    def total_royalties(self): 
        return sum([contract.royalties for contract in self.contracts()])
    #This method should return the total amount of royalties that the author has earned from all of their contracts.

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
#Test Book class has method contracts() that returns a list of its contracts

class Contract:
    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
   
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book  
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

# The date property should be a STRING that represents the date when the contract was signe
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

#the royalties property should be a NUMBER that represents the percentage of royalties that the author will receive for the book.
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)
    #This method should return all contracts that have the same date as the date passed into the method.