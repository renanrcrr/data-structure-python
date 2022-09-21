import random, copy

class Perceptron:
	def __init__(self, samples, outs, apprenticeship_fee=0.1, times=1000, threshold=-1):
		self.samples = samples 
		self.outs = outs 
		self.apprenticeship_fee = apprenticeship_fee 
		self.times = times 
		self.threshold = threshold 
		self.num_samples = len(samples) 
		self.num_sample = len(samples[0]) 
		self.weights = [] 

	def train(self):
		for sample in self.samples:
			sample.insert(0, -1)

		for i in range(self.num_sample):
			self.weights.append(random.random())

		self.weights.insert(0, self.threshold)

		num_times = 0

		while True:
			error = False 

			for i in range(self.num_samples):
				u = 0
			
				for j in range(self.num_sample + 1):
					u += self.weights[j] * self.samples[i][j]

				y = self.signal(u)

				if y != self.outs[i]:

					error_aux = self.outs[i] - y

					for j in range(self.num_sample + 1):
						self.weights[j] = self.weights[j] + self.apprenticeship_fee * error_aux * self.samples[i][j]

					error = True 

			num_times += 1

			if num_times > self.times or not error:
				break


	def test(self, sample, classe1, classe2):
		sample.insert(0, -1)

		u = 0
		for i in range(self.num_sample + 1):
			u += self.weights[i] * sample[i]

		y = self.signal(u)

		if y == -1:
			print('A sample pertence a classe %s' % classe1)
		else:
			print('A sample pertence a classe %s' % classe2)


	def signal(self, u):
		return 1 if u >= 0 else -1


print('\nA or B?\n')

samples = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], 
				[0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]

outs = [1, -1, -1, 1]

tests = copy.deepcopy(samples)

net = Perceptron(samples=samples, outs=outs,	
						apprenticeship_fee=0.1, times=1000)

net.train()

for test in tests:
	net.test(test, 'A', 'B')