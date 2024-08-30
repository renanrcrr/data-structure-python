class Stack:
	def __init__(self):
		self.stack = []
		self.len_stack = 0

	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1

	def pop(self):
		if not self.empty():
			self.stack.pop(self.len_stack - 1)
			self.len_stack -= 1

	def top(self):
		if not self.empty():
			return self.stack[-1]
		return None

	def empty(self):
		if self.len_stack == 0:
			return True
		return False
	
	def __str__(self):
		return f'Current stack => {self.stack}'

	def length(self):
		return self.len_stack

s = Stack()
print('Stack:' , s)
s.push(11)
print('New element added =>' , s.top())
s.push(21)
print('New element added =>' , s.top())
s.push(31)
print('New element added =>' , s.top())
print('Stack:' , s)
s.pop()
print(s.empty())
print('Stack:' , s)