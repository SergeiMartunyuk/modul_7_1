from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        blok_ = file.read()
        file.close()
        return blok_

    def add(self, *products):
        view = []
        file = open(self.__file_name, 'a+')
        file.seek(0)
        for line in file:
            name = line.split(', ')[0]
            view.append(name)
        for product in products:
            if product.name in view:
                print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
            else:
                file.write(f'{product}\n')
                view.append(product.name) and view.append(product.weight) and view.append(product.category)

        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())