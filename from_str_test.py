from from_str_decorator import from_str_init
import sys
import unittest

class from_strTests(unittest.TestCase):
	def test_basic_behaviour(self):
		a1 = A(1, 2)
		a2 = A("12")
		self.assertEqual(a1, a2)
		self.assertEqual(a2.one, 1)
		self.assertEqual(a2.two, 2)


	def test_one_str_param(self):
		b1 = B("1", 2)
		b2 = B("12")
		self.assertEqual(b1, b2)
		self.assertEqual(b2.one, '1')
		self.assertEqual(b2.two, 2)

	def test_kwargs(self):
		kwargs = {'kwone': 'kwone', 'kwtwo': 'kwtwo'}
		c1 = C(1, 2, **kwargs)
		c2 = C("12", **kwargs)
		self.assertEqual(c1, c2)
		self.assertEqual(c2.one, 1)
		self.assertEqual(c2.kwone, 'kwone')
		self.assertEqual(c2.kwtwo, 'kwtwo')
	
	def test_default_args(self):
		kwargs = {'kwone': 'kwone', 'kwtwo': 'kwtwo'}
		c1 = C(1, 2, **kwargs)
		c2 = C('12', **kwargs)
		self.assertEqual(c1, c2)
		self.assertEqual(c2.default, 'default')
	
	def test_literal_kwargs(self):
		kwargs = {'kwone': 'kwone', 'kwtwo': 'kwtwo'}
		c1 = C(1, 2, default='other', **kwargs)
		c2 = C('12',default='other', **kwargs)
		self.assertEqual(c1, c2)
		self.assertEqual(c2.default, 'other')

	def test_init_body(self):
		d1 = D(1, 2)
		d2 = D("12")
		self.assertEqual(d1.body, True)
		self.assertEqual(d2.body, True)

	def test_type_mismatch(self):
		try:
			e1 = E("12")
		except AssertionError as e:
			if '-v' in sys.argv: print(e)

class A:
	'''
	basic class requirements for from_str_init decorator
	'''
	one: int
	two: int

	@from_str_init
	def __init__(self, *args):
		pass

	def from_str(self, s):
		return (int(s[0]), int(s[1]))

	def __eq__(self, other):
		return self.one == other.one and self.two == other.two

class B:
	'''
	string parameter
	'''
	one: str
	two: int

	@from_str_init
	def __init__(self, *args):
		pass

	def from_str(self, s):
		return (s[0], int(s[1]))

	def __eq__(self, other):
		return self.one == other.one and self.two == other.two

class C:
	'''
	kwarg behaviour tests
	'''
	one: int
	two: int

	@from_str_init
	def __init__(self, *args, default='default', **kwargs):
		self.kwone = kwargs['kwone']
		self.kwtwo = kwargs['kwtwo']
		self.default = default

	def from_str(self, s):
		return (int(s[0]), int(s[1]))

	def __eq__(self, other):
		return self.one == other.one and self.two == other.two and self.kwone == other.kwone and self.kwtwo == other.kwtwo and self.default == other.default

class D:
	'''
	__init__ body functionality
	'''
	one: int
	two: int

	@from_str_init
	def __init__(self, *args):
		if '-v' in sys.argv: print(f'args given: {args}') # if verbose flag is passed to unittest
		self.body = True

	def from_str(self, s):
		return (int(s[0]), int(s[1]))

class E:
	'''
	from string type mis-match
	'''
	one: str
	two: str

	@from_str_init
	def __init__(self, *args):
		pass

	def from_str(self, s):
		return (int(s[0]), int(s[1]))
