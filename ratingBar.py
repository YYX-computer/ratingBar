import sys
def complete_string(n,string):
	while(len(string) < n):
		string += ' '
	return string

class ratingBar:
	def __init__(self,length,starting = '',ending = ''):
		self.length = length
		self.one = 100 / length
		self.n = len(str(self.length))
		self.starting = starting
		self.ending = ending
		sys.stdout.write('%s%s%s/%s|%s|0%% %s'%(self.starting,'|' * int(bool(self.starting)),n_digit(self.n,'0'),length,' ' * length，self.ending))
		sys.stdout.flush()
		self.len = 0
	def flush(self,length):
		if(length <= self.length):
			str1 = '#' * length + ' ' * (self.length - length)
			sys.stdout.flush()
			sys.stdout.write('\r%s%s%s/%s|%s|%s%% %s'%(self.starting,'|' * int(bool(self.starting)),n_digit(self.n,str(length)),self.length,str1,self.one * length，self.ending))
			if(length == self.length):
				sys.stdout.write('\n')
				sys.stdout.flush()
			self.len = length
		else:
			raise ValueError('index out of range')
	def count(self):
		self.len += 1
		self.flush(self.len)
