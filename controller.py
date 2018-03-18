from deal import deal

class one():
	def __init__(self, test=12):
		self.test = test;

	def foo(self, *args, **kwargs):
		print(f"one: {self.test}")

	def func1(self, *args, **kwargs):
		print("two!!")

class Controller:
	def __init__(self):
		self.one = one()
		self.two = one(2)
		self.fmap = {'one': self.one.foo, 'two': self.two.foo}
		self.tmap = {method_name: getattr(self.one, method_name) for method_name in dir(self.one) if callable(getattr(self.one, method_name)) and method_name[:1] != '_'}

	@staticmethod
	def _get_method_dict(obj):
		methods = {method: getattr(obj, method) for method in dir(obj) if callable(getattr(obj, method)) and method[0] != '_'}
		return methods

	def func(self, *args, **kwargs):
		for k, v in kwargs.items():
			print(k)

	def process_command(self, cmd, *args, **kwargs):
		ss_count = 0
		sub_cmd = ''
		if cmd in self.tmap: sub_cmd = cmd
		else:
			for map_cmd in self.tmap:
				if(map_cmd[:cmd.__len__()] == cmd):
					sub_cmd = map_cmd
					ss_count += 1
				if(ss_count >= 2): 
					sub_cmd = ''
					break
		
		if(sub_cmd): self.tmap[sub_cmd](*args, **kwargs)
	

if __name__ == "__main__":
	c = Controller()
	d, h1, h2, h3, h4 = deal()
	kwargs = {'one': 23}
	print(c.tmap) #["foo"]()
	c.fmap["one"](**kwargs)
	c.fmap["two"](**kwargs)
	print(Controller._get_method_dict(c))
	c.process_command('f')
	c.process_command('fun')
	c.process_command('foo')
