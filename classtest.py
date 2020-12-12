x = 100
class MyClass:
    i = 10
    x += 2
    xx = x + 2
    print('xx ;', xx)

    def price(self):
        y = self.i * x
        z = self.i * self.x
        print('price y: ', y)
        print('price z: ', z)
    
    def shop(self):
        self.price()
        MyClass.i = 20
        print("끝")
    
if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.shop()
    print(a.i, b.i)
    a.i = 2
    MyClass.i = 4
    print(a.i, b.i)

