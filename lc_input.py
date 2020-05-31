'''
The Lambda Calculus
'''

# Lambda Function
class Lambda:
	def __init__(self, func: str): # Input as "\x.\y.x*y"
		split = func.split(".")
		*inputs, mapping = split
		self.mapping = mapping.replace("I ", "")
		self.inputs = [i.replace("\\", "").replace("λ", "") for i in inputs]

		# The β reduction
		self.b = eval(fr"lambda {', '.join(self.inputs)}: {self.mapping}")

	def alpha(self, current: str, new: str): 		# The α conversion
		current, new = str(current), str(new)
		self.inputs = self.inputs.replace(current, new)
		self.mapping = self.mapping.replace(current, new)
		self.beta = eval(fr"lambda {', '.join(inputs)}: {mapping}")
		return self

	def beta(self, *inputs: list, verbose=False): 	# The β reduction
		inputs = [i for i in inputs]
		phrase = self.mapping
		for x, y in zip(self.inputs, inputs): phrase = phrase.replace(x, str(y))
		print(f"({self}){inputs} ~>ᵦ {phrase} =ᵦ {self.b(*inputs)}")
		return self.b(*inputs)


	''' PYTHON BOILER PLATE '''

	def __str__(self):
		return fr"λ{'.λ'.join(self.inputs)}.{self.mapping}"

	def __repr__(self):
		return str(self)

# More Boiler Plate
def list_now(x) -> list:
	if type(x) is int or type(x) is str:
		return [x]

	elif type(x) is tuple:
		return list(x)

	elif type(x) is list:
		return x

	else:
		raise ValueError


# Runtime
if __name__ == "__main__":
	while True:
		function, inp = input(">>>\t").split("|") 	# Input as function|inputs, e.g \x.\y.x+y|4,5
		X = Lambda(function)						
		x = list_now(eval(inp))         				
		X.beta(*x, verbose=True)