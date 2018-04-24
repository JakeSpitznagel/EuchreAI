from functools import wraps

def from_str_init(func):
	'''
		Decorator that auto initializes class annotations with positional arguments passed to __init__

		if class has a from_str method defined, a single string representation may be passed and will be interpreted by said method
		from_str needs to return a tuple of __init__ positional arguments
	
	'''
	@wraps(func)
	def f(self, *args, **kwargs): 
		func(self, *args)
		if 'from_str' not in self.__dir__(): return
		for name, val in zip(self.__annotations__, args):
			if self.__annotations__[name] == type(val):
				setattr(self, name, val)
			elif len(args) == 1 and type(args[0]) is str:
				for k, v in zip(self.__annotations__, self.from_str(val)):
					setattr(self, k, v)
				break
	return f
	

class A:
	one: int
	two: int

	@from_str_init
	def __init__(self, one=1, two=2):
		pass

	def from_str(self, s):
		'''
		return tuple of interpreted positional args
		'''
		return (s[:-1], s[-1:])

	def callable(self, arg):
		print(arg)
		return True


class B:
	@from_str_init
	def __init__(self, arr:A):
		self.arr = arr

	def from_str(*args):
		return args[1]


if __name__ == '__main__':
	a = A(1, 2)
	a2 = A('12')
	#b = B([1, 2, 3, 4])
	print(a.two)
	print(a.one)
	print(a2.one)
	print(a2.two)
