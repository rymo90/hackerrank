from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def display():
        pass


class MyBook(Book):
    def display(self):
        super(Book, self).__init__()
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input()
author = input()
price = int(input())
newNovel = MyBook(title, author, price)
newNovel.display()
