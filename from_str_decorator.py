from functools import wraps

def from_str_init(func):
	'''
		Decorator that auto initializes class annotations with positional arguments passed to __init__
		kwargs may still be passed and handled by class's  __init__

		if class has a from_str method defined, a single string representation may be passed and will be interpreted by said method
		from_str needs to return a tuple of __init__ positional arguments
	
	'''
	@wraps(func)
	def inner(self, *args, **kwargs): 
		func(self, *args, **kwargs)
		if 'from_str' not in self.__dir__(): return
		for name, val in zip(self.__annotations__, args):
			if len(args) == 1 and type(args[0]) is str:
				for k, v in zip(self.__annotations__, self.from_str(val)):
					assert self.__annotations__[k] == type(v), f'from_str type does not match expected type, expected: {self.__annotations__[k]}, actual: {type(v)}'
					setattr(self, k, v)
				break
			elif self.__annotations__[name] == type(val):
				setattr(self, name, val)
	return inner
	

