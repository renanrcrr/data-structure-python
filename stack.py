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

	def length(self):
		return self.len_stack

s = Stack()

s.push(11)
s.push(21)
s.push(31)

print(s.top())