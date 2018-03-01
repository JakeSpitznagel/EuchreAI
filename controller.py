from deal import deal

class one():
    def __init__(self, test=12):
        self.test = test;

    def foo(self, *args, **kwargs):
        print(f"one: {self.test}")

class Controller:
    def __init__(self):
        self.one = one()
        self.two = one(2)
        self.fmap = {'one': self.one.foo, 'two': self.two.foo}
        self.tmap = {method_name: getattr(self.one, method_name) for method_name in dir(self.one) if callable(getattr(self.one, method_name)) and method_name[:2] != '__'}

    def func(self, *args, **kwargs):
        for k, v in kwargs.items():
            print(k)

if __name__ == "__main__":
    c = Controller()
    d, h1, h2, h3, h4 = deal()
    print([method_name for method_name in dir(h1) if callable(getattr(h1, method_name))])
    kwargs = {'one': 23}
    print(c.tmap) #["foo"]()
    c.fmap["one"](**kwargs)
    c.fmap["two"](**kwargs)
