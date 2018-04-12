class Price:
    """
    Descriptor Price, which do not allow create
    Book with price lower than 0 and more than 100
    """
    def __init__(self,label):
        self.label = label
    def __get__(self,instance,owner):
        return instance.__dict__[self.label]
    def __set__(self,instance,value):
        assert 0 < value < 100, "Price must be between 0 and 100"
        instance.__dict__[self.label] = value

class Book:
    """
    Class Book
    :param - autor
    :type - script
    :param - name
    :type - script
    :param - price
    :type - int
    """
    price = Price('price')
    def __init__(self,autor,name,price):
        self.autor = autor
        self.name = name
        self.price = price

if __name__ == '__main__':
    b = Book('kkk','ooo', 12)
    s = Book('kkk','ttt',13)
    print(b.name)
    print(s.name)
    print(b.price)
    print(s.price)
    print(b.price)